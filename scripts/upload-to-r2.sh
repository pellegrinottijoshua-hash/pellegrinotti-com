#!/usr/bin/env bash
# Upload pellegrinotti.com media to Cloudflare R2.
# Run from ~/jayl-studio. Requires: brew install awscli
#
# 1) Pull real R2 credentials locally (never through the Claude Code sandbox):
#      vercel env pull .env.local --environment=production
# 2) Run this script:
#      bash scripts/upload-to-r2.sh
set -euo pipefail
cd "$(dirname "$0")/.."

if [ -f .env.local ]; then
  set -a; source .env.local; set +a
fi

: "${R2_ACCOUNT_ID:?Missing R2_ACCOUNT_ID — did you run: vercel env pull .env.local}"
: "${R2_ACCESS_KEY_ID:?Missing R2_ACCESS_KEY_ID}"
: "${R2_SECRET_ACCESS_KEY:?Missing R2_SECRET_ACCESS_KEY}"
: "${R2_BUCKET_NAME:?Missing R2_BUCKET_NAME}"

export AWS_ACCESS_KEY_ID="$R2_ACCESS_KEY_ID"
export AWS_SECRET_ACCESS_KEY="$R2_SECRET_ACCESS_KEY"
ENDPOINT="https://${R2_ACCOUNT_ID}.r2.cloudflarestorage.com"

echo "→ Desktop hero photos (assets/hero/*.jpg)"
aws s3 sync assets/hero s3://"$R2_BUCKET_NAME"/hero \
  --exclude "*" --include "*.jpg" \
  --endpoint-url "$ENDPOINT" --cache-control "public, max-age=31536000, immutable"

echo "→ Mobile hero videos (01.mp4 … 12.mp4, uncompressed)"
aws s3 sync assets/hero/mobile-video-src s3://"$R2_BUCKET_NAME"/hero/mobile-video \
  --exclude "posters/*" \
  --endpoint-url "$ENDPOINT" --cache-control "public, max-age=31536000, immutable" \
  --content-type "video/mp4"

echo "→ Mobile hero video posters (first-frame stills)"
aws s3 sync assets/hero/mobile-video-src/posters s3://"$R2_BUCKET_NAME"/hero/mobile-video/posters \
  --endpoint-url "$ENDPOINT" --cache-control "public, max-age=31536000, immutable" \
  --content-type "image/jpeg"

echo "→ Jayl Video drawer clips"
for f in duel.mp4 therug1.mp4 therug2.mp4 therug3.mp4 therug5.mp4 therug6.mp4 therug7.mp4 therug8.mp4 therug9.mp4 therug10.mp4 therug11.mp4 lei-chi-e-web.mp4; do
  aws s3 cp "assets/$f" "s3://$R2_BUCKET_NAME/video/$f" \
    --endpoint-url "$ENDPOINT" --cache-control "public, max-age=31536000, immutable" \
    --content-type "video/mp4"
done

echo "✓ Done. Public base URL should be: $R2_PUBLIC_URL"
