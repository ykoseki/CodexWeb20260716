from datetime import date
import textwrap

OUT='jinden_company_profile_10p.pdf'
W,H=842,595
slides=[
('神町電子株式会社\n企業紹介資料','山形県東根市を拠点に、EMS・製品企画開発・OA商品販売・保育園運営を展開\n作成日：2026年7月16日 / 出典：https://www.jinden.jp/'),
('1. 会社概要','会社名：神町電子株式会社\n設立：1979年9月11日 / 資本金：1,000万円\n代表者：代表取締役 板垣 政則\n従業員数：90名\n本社：山形県東根市一本木1-1-7\n大森工場：山形県東根市大字東根甲7057-174'),
('2. 企業メッセージ','1979年の設立以来、精密メカトロニクス技術をコアに製造技術力を蓄積。\n信頼性の高い品質力を礎に、モノづくりで顧客と地域社会の発展に貢献。\n企画段階から設計開発・生産・出荷まで、ワンストップ対応できる企業を目指す。'),
('3. 事業領域','電子機器受託製造サービス（EMS、製品製造請負）\n製品企画開発サービス（3D-CAD設計、装置・治工具・部品設計製作）\n商品販売（リサイクルトナー、OA機器、データ消去サービス）\n保育園の運営'),
('4. EMS・製造受託','金融端末製品の製造・修理\n介護浴槽装置、リハビリテーション機器の製造\n電子顕微鏡など電子光学機器ユニットの製造\n医用機器・自動分析装置の製造\nその他製品の組立・検査請負'),
('5. 工場の強み','「品質第一」をモットーに、高品質な製品を提供。\n部品調達から管理、組立製造、出荷試験・検査まで一貫対応。\n改善活動・小集団活動（JQC）・6S活動・目標管理制度により、安定品質、リードタイム短縮、コスト削減を実現。'),
('6. 製品企画開発室','顧客ニーズを形にする少数精鋭のスペシャリスト集団。\n構想設計、機械設計、電気設計、ソフト設計、システム設計、部品調達、組立調整、納品設置、保守メンテナンスまで担う。\n主な自社製品：野菜加工機、PRS装置。'),
('7. 開発・製造実績','大量処理型HDDデータ消去装置\n3D積層造形装置用ガス置換型ブラスト装置 / 3D自動ブラストシステム\nガス置換型金属粉末搬送システム / 金属粉末自動分級システム\nウェットブラスト装置、特殊研磨装置\n工場生産管理帳票システム開発（ペーパーレス化）'),
('8. 商品販売・地域密着サービス','リサイクルトナー・インク・リボン等サプライ商品の販売\nコピー機・プリンター・パソコン等OA周辺機器の販売\nHDD・SSDデータ消去サービス\n地域密着型の営業販売で、オフィス業務を支援。'),
('9. 環境・人材・お問い合わせ','ISO14001、医療機器製造業の認定登録。\n基本理念：「豊かで美しい自然環境を保全し、環境にやさしい企業活動を行う」\n地域未来牽引企業に選定、子育て応援企業の認定も取得。\nTEL 本社：0237-43-2211 / 大森工場：0237-42-4441\n営業時間：8:10～17:10')]

def esc(s): return s.replace('\\','\\\\').replace('(','\\(').replace(')','\\)')
def tj(s): return '<'+s.encode('utf-16-be').hex().upper()+'>'
objs=[]
def add(x): objs.append(x); return len(objs)
font=add('<< /Type /Font /Subtype /Type0 /BaseFont /HeiseiKakuGo-W5 /Encoding /UniJIS-UTF16-H /DescendantFonts [<< /Type /Font /Subtype /CIDFontType0 /BaseFont /HeiseiKakuGo-W5 /CIDSystemInfo << /Registry (Adobe) /Ordering (Japan1) /Supplement 2 >> /FontDescriptor << /Type /FontDescriptor /FontName /HeiseiKakuGo-W5 /Flags 6 /FontBBox [0 -200 1000 900] /ItalicAngle 0 /Ascent 900 /Descent -200 /CapHeight 700 /StemV 80 >> >>] >>')
page_ids=[]; content_ids=[]
for i,(title,body) in enumerate(slides,1):
    stream=[]
    stream.append('0.95 0.98 1 rg 0 0 842 595 re f')
    stream.append('0.02 0.20 0.38 rg 0 535 842 60 re f')
    stream.append('BT /F1 28 Tf 50 555 Td 1 1 1 rg '+tj(title.split('\n')[0])+' Tj ET')
    if '\n' in title:
        stream.append('BT /F1 17 Tf 50 500 Td 0.02 0.20 0.38 rg '+tj(title.split('\n')[1])+' Tj ET')
    y=455
    for para in body.split('\n'):
        lines=textwrap.wrap(para, width=42, break_long_words=False) or ['']
        for line in lines:
            prefix='• ' if not any(line.startswith(x) for x in ['会社名','設立','代表者','従業員数','本社','大森','作成日','TEL','営業時間','ISO']) and i not in [1,3] else ''
            stream.append(f'BT /F1 18 Tf 75 {y} Td 0.05 0.05 0.05 rg '+tj(prefix+line)+' Tj ET')
            y-=34
        y-=8
    stream.append(f'BT /F1 11 Tf 735 25 Td 0.3 0.3 0.3 rg '+tj(f'{i}/10')+' Tj ET')
    stream.append('0.02 0.20 0.38 RG 50 60 742 0 l S')
    data='\n'.join(stream).encode('ascii')
    content_ids.append(add(f'<< /Length {len(data)} >>\nstream\n'+data.decode('ascii')+'\nendstream'))
    page_ids.append(add(''))
pages=add('')
for idx,pid in enumerate(page_ids):
    objs[pid-1]=f'<< /Type /Page /Parent {pages} 0 R /MediaBox [0 0 {W} {H}] /Resources << /Font << /F1 {font} 0 R >> >> /Contents {content_ids[idx]} 0 R >>'
objs[pages-1]='<< /Type /Pages /Kids ['+' '.join(f'{p} 0 R' for p in page_ids)+f'] /Count {len(page_ids)} >>'
catalog=add(f'<< /Type /Catalog /Pages {pages} 0 R >>')
with open(OUT,'wb') as f:
    f.write(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n')
    offs=[0]
    for n,o in enumerate(objs,1):
        offs.append(f.tell()); f.write(f'{n} 0 obj\n{o}\nendobj\n'.encode('ascii'))
    x=f.tell(); f.write(f'xref\n0 {len(objs)+1}\n0000000000 65535 f \n'.encode())
    for off in offs[1:]: f.write(f'{off:010d} 00000 n \n'.encode())
    f.write(f'trailer << /Size {len(objs)+1} /Root {catalog} 0 R >>\nstartxref\n{x}\n%%EOF\n'.encode())
print(OUT)
