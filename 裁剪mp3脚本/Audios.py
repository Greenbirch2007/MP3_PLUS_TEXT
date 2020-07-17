from pydub import AudioSegment
# 可以裁剪mp3，wav文件
file_name = "t.mp3"
sound = AudioSegment.from_mp3(file_name)
start_time = "01:01"
stop_time = "01:18"
print( "time:",start_time,"~",stop_time)
start_time = (int(start_time.split(':')[0])*60+int(start_time.split(':')[1]))*1000
stop_time = (int(stop_time.split(':')[0])*60+int(stop_time.split(':')[1]))*1000
print( "ms:",start_time,"~",stop_time)
word = sound[start_time:stop_time]
save_name = "w.mp3"+file_name[6:]
print(save_name)
word.export(save_name, format="mp3",tags={'artist': 'AppLeU0', 'album': save_name[:-4]})
