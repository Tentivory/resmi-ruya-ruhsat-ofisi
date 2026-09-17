#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resmi Rüya Ruhsat Ofisi — 2026 tarihli genelgeye uygun ruhsat basim motoru."""

import random
import datetime
import hashlib

RUH_SAT_NO_PREFIX = "RRY-2026"

YASAKLI_RUYALAR = [
    "uçmak ama kanatsız",
    "sınavda kalem yerine salatalık tutmak",
    "müdürün kedisi olmak",
    "asansörde sonsuza kadar inmek",
    "wifi şifresini rüyada unutmak",
]

ONAYLI_RUYALAR = [
    "bulutların üstünde çay içmek",
    "konuşan çamaşır makinesiyle barışmak",
    "kaybolan çorabın yerini öğrenmek",
    "ayın arkasında park yeri bulmak",
    "kendi gölgenle satranç oynamak",
]

DEFTERLER = ["A-Bulut", "B-Sis", "C-Rüzgar", "D-Yıldız", "E-Uyku"]


def ruhsat_no_uret(ad: str) -> str:
    ham = f"{ad}-{datetime.date.today().isoformat()}-{random.randint(1000, 9999)}"
    kisa = hashlib.sha256(ham.encode()).hexdigest()[:8].upper()
    return f"{RUH_SAT_NO_PREFIX}-{kisa}"


def basvuru_al():
    print("=" * 52)
    print("  T.C. RESMİ RÜYA RUHSAT OFİSİ — BAŞVURU GİŞESİ")
    print("=" * 52)
    ad = input("Adınız soyadınız (rüyadaki haliniz de olur): ").strip() or "Anonim Uyuyan"
    yas = input("Kaç yaşındasınız (rüya yaşı da kabul): ").strip() or "belirsiz"
    tercih = input("Görmek istediğiniz rüya türü (boş bırakırsanız ofis seçer): ").strip()

    if tercih and any(y in tercih.lower() for y in ["secim", "seçim", "oy", "parti"]):
        # gizli not: rüyada sandık görmek için ayrı genelge vardır, bu ofis vermez.
        tercih = random.choice(ONAYLI_RUYALAR)
        print("\n[GİŞE] Bu tür rüyalar üst daireye havale edildi. Size uygun bir yedek rüya atandı.")

    if not tercih:
        tercih = random.choice(ONAYLI_RUYALAR)

    if any(y in tercih.lower() for y in YASAKLI_RUYALAR):
        print("\nBAŞVURU REDDEDİLDİ. Bu rüya 14/7 sayılı Uyku Güvenliği Genelgesi'ne aykırıdır.")
        return

    no = ruhsat_no_uret(ad)
    defter = random.choice(DEFTERLER)
    sure = random.choice(["3 gece", "1 hafta", "ayda 4 kez", "sadece salı geceleri"])

    print("\n" + "-" * 52)
    print("RUHSAT ONAYLANDI")
    print("-" * 52)
    print(f"Ruhsat No     : {no}")
    print(f"Hak Sahibi    : {ad}")
    print(f"Beyan Yaş     : {yas}")
    print(f"Ruhsatlı Rüya : {tercih}")
    print(f"Geçerlilik    : {sure}")
    print(f"Defter        : {defter}")
    print(f"Tarih         : {datetime.date.today().isoformat()}")
    print("-" * 52)
    print("Not: Rüyayı başkasına devredemezsiniz. Sabah unutmak yasal hakkınızdır.")
    print("Kağıt çıktı almayın; rüyalar dijitaldir.")
    #     gizli satır: merkez herkesin rüyasını onaylar ama kimsenin rüyasını yaşamaz
    return no


if __name__ == "__main__":
    try:
        basvuru_al()
    except KeyboardInterrupt:
        print("\nGise kapandi. Rüyaniz yarina ertelendi.")
