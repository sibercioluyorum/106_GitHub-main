# HaberVerileriToplamaVeOnisleme_106

Bu proje, haber sayfalarından başlıkları ve haber metinlerini toplayıp bu metinlere önişleme(NLP) adımlarını uygulayan bir araçtır. <br/><br/><br/>

## Özellikler

- **Haber Toplama**: Çeşitli haber sitelerinden başlık ve metin toplanır.
- **Önişleme**: Toplanan metinlere durdurma kelimelerini kaldırma, küçük harfe çevirme , kök alma gibi NLP önişleme işlemleri uygulanır.
- **Veri Çıkışı**: İşlenmiş metinler xlsx formatında kaydedilir. <br/><br/><br/>

  

## Gereksinimler

- Python 3.13
- Selenium (veri toplama için)
- NLTK  (doğal dil işleme işlemleri için)
- openpyxl (exel dosyası olarak kaydetme)
- pandas     <br/><br/><br/>

Gereksinimleri yüklemek için:

```bash
pip install -r requirements.txt
```



## Kurulum
1. Sanal ortam oluşturun ve etkinleştirin:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  
   ```
   veya
   ```bash
   myenv\Scripts\activate
   ```
 
