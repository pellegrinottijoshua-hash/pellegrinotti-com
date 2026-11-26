"""Copia e alleggerisce le immagini scelte per le schede Zack e The Rug (JPEG, lato lungo limitato)."""
import os
from PIL import Image

Z = '/Users/jpelle/Desktop/zack the duck/'
R = '/Users/jpelle/Desktop/the rug/'
OUT_Z = '/Users/jpelle/pellegrinotti-com/zack/assets/v3/'
OUT_R = '/Users/jpelle/pellegrinotti-com/therug/assets/v3/'
GP = Z + 'gag 3d corte/presentazioni-personaggi/panna/'
EP = Z + 'gag 3d corte/episodi-3d/frame-17nov/panna/'
L2 = Z + 'gag 3d corte/lotto-2/frame/'
MU = Z + 'museo/'

ZACK = {
    # la premessa
    'tratto': (Z + 'characters/tratto.png', 1100),
    'zack-piuma': (GP + 'z1.png', 1100),
    # arte e cibo
    'arte-teiera': (MU + 'oggetti surrealisti/hf_20261004_223548_06669f7c-67f3-4fe9-9d7d-545861d771eb.png', 1200),
    'arte-sedia': (MU + 'oggetti surrealisti/hf_20261004_223006_d96dce2c-7d50-44e3-a34c-9811e9f15004.png', 1200),
    'arte-tazza': (MU + 'oggetti surrealisti/hf_20261004_223244_5d179806-30a8-4c81-8c83-c39bbb14b03a.png', 1200),
    'arte-telefono': (MU + 'oggetti surrealisti/oggetti surrealisti.png', 1200),
    'arte-busti': (MU + 'altri stili/hf_20260922_100326_469bb302-8717-4d9d-8be0-9c53eed664fc.png', 1200),
    'arte-ritratto': (MU + 'altri stili/hf_20260922_165314_e55b4468-a6c1-4e6e-a261-95a022d8a424.png', 1200),
    'arte-violino': (MU + 'oggetti surrealisti/hf_20261004_234015_2ec5da80-8b2d-4590-a847-faca9d0422d2.png', 1200),
    'arte-scultura': (MU + 'figure umanoidi /hf_20261004_202540_0829f2b2-0c44-4448-bfe2-bf1106876b77.png', 1200),
    'arte-vasi': (MU + 'vasi/hf_20261005_115402_ade567e2-1e17-4503-b5ee-6a0d18e7dc8e.png', 1200),
    'cibo-torta': (EP + '1 THIRD_panna.png', 900),
    'cibo-croissant': (GP + 'f1.png', 900),
    # il cast
    'cast-piccione': (Z + 'characters/ipigeon.png', 900),
    'cast-gabbiano': (Z + 'characters/iseagull.png', 900),
    'cast-falena': (Z + 'characters/imoth.png', 900),
    'cast-gatto': (Z + 'characters/icat.png', 900),
    'cast-formica': (Z + 'characters/iant.png', 900),
    'cast-tartaruga': (GP + 't1.png', 900),
    # le gag
    'gag-01': (EP + '1 FIRST_panna.png', 720), 'gag-02': (EP + '4 TERZA_panna.png', 720),
    'gag-03': (EP + '3 SECOND_panna.png', 720), 'gag-04': (EP + '2 FIRST_panna.png', 720),
    'gag-05': (Z + 'gag 3d corte/lotto-3/frame/23-il-tocco-finale/panna/G23_panna.png', 720),
    'gag-06': (GP + 't2.png', 720), 'gag-07': (GP + 'm.png', 720),
    'gag-08': (L2 + '18-foto-di-gruppo/panna/G18-4D_panna.png', 720),
    'gag-09': (L2 + '11-dietro-le-quinte/panna/G11-2_panna.png', 720),
    'gag-10': (L2 + '12-lepre-e-tartaruga/panna/G12A_panna.png', 720),
    'gag-11': (L2 + '10-servizio-fotografico/panna/G10C_panna.png', 720),
    'gag-12': (GP + 'c2.png', 720), 'gag-13': (GP + 'p2.png', 720), 'gag-14': (GP + 'g5.png', 720),
    'gag-15': (GP + 't3.png', 720), 'gag-16': (L2 + '18-foto-di-gruppo/panna/G18-1_panna.png', 720),
    # il libro
    'libro-copertina': (Z + 'art books for kids/kdp/copertina.png', 1400),
    'libro-p1': (Z + 'art books for kids/pagine/1.png', 800), 'libro-p11': (Z + 'art books for kids/pagine/11.png', 800),
    'libro-p13': (Z + 'art books for kids/pagine/13.png', 800), 'libro-p15': (Z + 'art books for kids/pagine/15.png', 800),
    # da indossare
    'merch-1': (Z + 'merch/tshirt/hf_20261115_235024_32734cde-8e5b-4caf-81d7-0c88bcaa37ab.png', 1000),
    'merch-2': (Z + 'merch/tshirt/hf_20261115_235109_e2530a5a-7fdf-4096-b684-a01ac7217108.png', 1000),
    'merch-3': (Z + 'merch/tshirt/hf_20261115_235317_868717a8-ed56-4c3e-a1b0-49ecb87c1f1d.png', 1000),
}

RUG = {
    'citta': (R + 'locations/citta1.png', 2000),
    'poltrona': (R + 'characters/hf_20260718_001223_3f2a19d7-a62c-47b8-8949-bc4dd0ec96e2.png', 1400),
    'sheet': (R + 'characters/therugsheet.png', 1800),
    'volto': (R + 'scene/therug2.png', 1600),
    'luogo-strada': (R + 'locations/strada1.png', 1600), 'luogo-piazza': (R + 'locations/piazza.png', 1600),
    'luogo-incrocio': (R + 'locations/incrocio.png', 1600), 'luogo-tetto': (R + 'locations/soffitto.png', 1600),
    'luogo-via': (R + 'locations/via.png', 1600), 'luogo-citta': (R + 'locations/citta2.png', 1600),
    'luogo-buca': (R + 'locations/dettagliostrada.png', 1600),
    'schiaffo-1': (R + 'frame POD/POD03_mano_fisheye.png', 1600),
    'schiaffo-2': (R + 'frame POD/POD07_ecu_occhi_alien1.png', 1600),
    'schiaffo-3': (R + 'startframes/CUT_a5_4s5_pre_ultimo_colpo.jpg', 1600),
    'schiaffo-4': (R + 'schiaffomaster1.png', 1600),
    'schiaffo-5': (R + 'frame POD/POD04_ecu_schiaffo_boss.png', 1600),
    'schiaffo-6': (R + 'startframes/LAST_a10.jpg', 1600),
    'alieno-a1': (R + 'characters/alien1cu.png', 900),
    'alieno-left': (R + 'scene/hf_20260804_005410_ff30f0d8-f816-4898-b742-f3cbaa22b8a1.png', 900),
    'alieno-gag': (R + 'scene/hf_20260804_005955_26117a2c-9a92-4ab2-80a1-2b4b3c8d0e5e.png', 900),
    'alieno-rock': (R + 'scene/hf_20260804_010456_d2e37636-e864-47da-9cab-2c0c7c1e6b0b.png', 900),
    'alieno-right': (R + 'scene/hf_20260804_011202_648b5157-12b8-4ed4-855f-9c7b0b1c1f5e.png', 900),
    'alieno-boss': (R + 'scene/hf_20260804_011402_f0336fd6-39f5-40ad-ae49-8a0f2f0c2b49.png', 900),
    'poster-volo': (R + 'frame POD/POD05_tappeto_volante_citta.png', 1400),
    'poster-ufo': (R + 'frame POD/POD02_ufo_alieni_appesi.png', 1400),
    'poster-ombra': (R + 'frame POD/POD08_rug_spalle_ombra_lunga.png', 1400),
    'poster-controsole': (R + 'frame POD/POD01_rug_spalle_mantello_controsole.png', 1400),
}

def trova(path):
    """I nomi lunghi di Higgsfield li cerco per prefisso, nella cartella e nelle sorelle."""
    if os.path.exists(path):
        return path
    base = os.path.basename(path)[:24]
    radice = os.path.dirname(os.path.dirname(path))
    for d, _, fs in os.walk(radice):
        for f in fs:
            if f.startswith(base):
                return os.path.join(d, f)
    return None

def esporta(mappa, out):
    os.makedirs(out, exist_ok=True)
    for nome, (src, lato) in mappa.items():
        p = trova(src)
        if not p:
            print('MANCA', nome, src); continue
        im = Image.open(p).convert('RGB')
        k = min(1, lato / max(im.size))
        if k < 1:
            im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
        im.save(out + nome + '.jpg', quality=80, optimize=True, progressive=True)
        print(nome, im.size, os.path.getsize(out + nome + '.jpg') // 1024, 'KB')

esporta(ZACK, OUT_Z)
esporta(RUG, OUT_R)
