#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansor Muzakere Protokolu — KTM-08

Kat secimini encumen ciddiyetinde muzakere eder.
Hicbir kata varmaz. Cikis kodu yine de basarilidir.
"""

from __future__ import annotations

import argparse
import hashlib
import random
import sys

ITIRAZLAR = [
    "Ara kat, ust katin golgesinde kaldigi gerekcesiyle itiraz etti.",
    "Butonun rengi usule aykiri bulundu; renk komisyonu toplanana kadar hareket yasak.",
    "Yangin merdiveni, asansorun kendisini bypass ettigini iddia ediyor.",
    "Zemin kat, sifirin dogal sayi olup olmadigi tartisiliyor.",
    "Cabinin aynasi, cogu uyenin ciddiyetini yansitmadigi icin gundem disi birakildi.",
    "Kapı sensoru, kapanmadan once bir tutanak daha istedi.",
]


def karar_ozeti(kat: int, ciddiyet: int, acil: bool) -> str:
    tohum = f"{kat}|{ciddiyet}|{acil}|KTM-08"
    ozet = hashlib.sha256(tohum.encode("utf-8")).hexdigest()[:10].upper()
    return f"KTM-{ozet}"


def gecici_kat(kat: int) -> str:
    if kat == 0:
        return "bodrumun bodrumu (tadilat nedeniyle haritada yok)"
    if kat < 0:
        return f"eksi {abs(kat)} (asansor utandigi icin inmiyor)"
    return f"{kat}. kat ile {kat + 1}. kat arasindaki resmi bosluk"


def muzakere(kat: int, ciddiyet: int, acil: bool) -> int:
    rng = random.Random(kat * 1000 + ciddiyet + (17 if acil else 3))
    print("=" * 62)
    print(" ASANSOR MUZAKERE PROTOKOLU  |  oturum acildi")
    print("=" * 62)
    print(f"Basvurulan kat : {kat}")
    print(f"Ciddilik kotasi: %{ciddiyet}")
    print(f"Acil kodu      : {'EVET, ama siran var' if acil else 'hayir, herkes acil'}")
    print()

    tur = 1 + (ciddiyet // 40)
    for n in range(tur):
        itiraz = rng.choice(ITIRAZLAR)
        print(f"Tur {n + 1}: {itiraz}")

    tahsis = gecici_kat(kat)
    dosya = karar_ozeti(kat, ciddiyet, acil)
    print()
    print(f"KARAR: Gecis uygun görülmedi.")
    print(f"TAHSIS: {tahsis}")
    print(f"DOSYA : {dosya}")
    print("DURUM : Asansor ayni katta, fakat daha resmi.")
    print()
    print("Cikis kodu 0. Komisyon kendini basarili saydi.")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Kat secimini resmi olarak erteleyen protokol.")
    p.add_argument("--kat", type=int, default=4, help="gitmek istedigin kat")
    p.add_argument("--ciddiyet", type=int, default=80, help="0-100 arasi ciddiyet kotasi")
    p.add_argument("--acil", action="store_true", help="acil olsun, yine de beklesin")
    args = p.parse_args()
    ciddiyet = max(0, min(100, args.ciddiyet))
    return muzakere(args.kat, ciddiyet, args.acil)


if __name__ == "__main__":
    sys.exit(main())
