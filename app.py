from flask import Flask, request, render_template
import summariser
import translator
import video_info

app=Flask(__name__)
app.secret_key='123-456-789'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/project')
def projectpage():
    return render_template('url.html')


@app.route('/output',methods=['GET','POST'])
def summarise():
    if request.method=='POST':
        url=request.form['url']
        max_len=request.form.get('max_len','')
        # lang=request.form['lang']
        if not max_len.isdigit():
            max_len=150
        else:
            max_len=int(max_len)
        if url[11]=='.':
            video_id = url.split('=')[1]
        else:
            video_id = url.split('?')[0][17:]
        title=video_info.get_video_title(video_id)
        # transcript=video_info.get_video_transcript(video_id)
        result=summariser.summarise(video_id, max_len)
        summary=result[0]
        transcript=result[1]
        langs={
                'en':'English', 'hi':'Hindi', 'mr':'Marathi',\
                'gu':'Gujarati', 'ml':'malayalam', 'kn':'Kannada',\
                'bn':'Bengali', 'pa':'Punjabi', 'ta':'Tamil',\
                'te':'Telugu', 'ar':'Arabic', 'fr':'French',\
                'de':'German', 'ja':'Japanese', 'ru':'Russian', 'es':'Spanish'}
        
        summary_hi=translator.translate_to_hindi(summary)
        summary_mr=translator.translate_to_marathi(summary)
        summary_guj=translator.translate_to_guj(summary)
        summary_malaya=translator.translate_to_malayalam(summary)
        summary_kan=translator.translate_to_kannada(summary)
        summary_ben=translator.translate_to_bengali(summary)
        summary_pj=translator.translate_to_punjabi(summary)
        summary_tam=translator.translate_to_tamil(summary)
        summary_tel=translator.translate_to_telugu(summary)
        summary_ar=translator.translate_to_arabic(summary)
        summary_french=translator.translate_to_french(summary)
        summary_germ=translator.translate_to_german(summary)
        summary_jap=translator.translate_to_japanese(summary)
        summary_rus=translator.translate_to_russian(summary)
        summary_sp=translator.translate_to_spanish(summary)
        
        return render_template('output.html', transcript=transcript, vid_title=title, summary_en=summary,\
                               summary_hi=summary_hi, summary_mr=summary_mr, summary_guj=summary_guj,\
                               summary_malaya=summary_malaya, summary_kan=summary_kan, summary_ben=summary_ben,\
                               summary_pj=summary_pj,  summary_tam=summary_tam, summary_tel=summary_tel,\
                               summary_ar=summary_ar, summary_french=summary_french, summary_germ=summary_germ,\
                               summary_jap=summary_jap, summary_rus=summary_rus, summary_sp=summary_sp)
    else:
        return render_template('output.html')

if __name__=="__main__":
    app.run()