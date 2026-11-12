import json

def jalankan_fc(file_json):
    with open(file_json, 'r') as f:
        kb = json.load(f)

    print(f"\n--- {kb['judul']} ---")
    print("Jawab pertanyaan berikut dengan (y/t).")

    semua_jika = set(f for aturan in kb['aturan'] for f in aturan['jika'])
    semua_maka = set(aturan['maka'] for aturan in kb['aturan'])
    fakta_dasar = semua_jika - semua_maka

    memori = set()
    fakta_awal = []
    for i, fakta in enumerate(sorted(fakta_dasar), 1):
        jawaban = input(f"{i}. Apakah {fakta}? (y/t) > ").lower()
        if jawaban == 'y':
            memori.add(fakta)
            fakta_awal.append(fakta)

    print(f"\nFakta awal: {', '.join(fakta_awal) if fakta_awal else 'Tidak ada'}\n")

    aturan_terpakai = [] 
    siklus = 1
    
    while True:
        ada_tambahan = False
        for aturan in kb['aturan']:
            if aturan['maka'] in memori:
                continue
            
            syarat_jika = set(aturan['jika'])
            cocok = False
            
            if aturan['mode'] == 'dan':
                cocok = syarat_jika.issubset(memori)
            elif aturan['mode'] == 'atau':
                cocok = len(syarat_jika.intersection(memori)) > 0
                
            if cocok:
                memori.add(aturan['maka'])
                alasan_str = f"{aturan['maka']} <- {aturan['id']} ({', '.join(aturan['jika'])})"
                aturan_terpakai.append(alasan_str)
                print(f"Siklus {siklus}: {aturan['id']} -> {aturan['maka']}")
                ada_tambahan = True
                siklus += 1
                break
                
        if not ada_tambahan:
            print(f"Siklus {siklus}: tidak ada aturan baru, berhenti\n")
            break

    kesimpulan = memori.intersection(semua_maka)
    kesimpulan_akhir = [k for k in kesimpulan if not any(k in a['jika'] for a in kb['aturan'])]
    
    if kesimpulan_akhir:
        print(f"Kesimpulan: {', '.join(kesimpulan_akhir)}")
    else:
        print("Kesimpulan: tidak ada (kasus negatif)")
        
    print("Alasan:")
    if aturan_terpakai:
        for alasan in reversed(aturan_terpakai):
            print(f"  {alasan}")
    else:
        print("  Tidak ada aturan yang terpenuhi.")
        
    print(f"\nCatatan: {kb['batas']}")

if __name__ == "__main__":
    jalankan_fc('kb_jaringan.json')