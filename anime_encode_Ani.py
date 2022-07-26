#Moment Google Drive & FFMPEG ENCODE
"""

#@title <Center>Mount Google Drive </Center>
#@markdown <Center> <img src="https://kstatic.googleusercontent.com/files/e20dbc1db7b6eab22fb2d07df8043f8a74b301dbb8c176e6a1992b2dc229c5ae94b5c260cf549c41712fa40b7e639166c6a8461303a27c2a3b9c55b8ca155ec3" class="icon" alt="Icon">
#@markdown <h6> Made In Ani Animesh </h6>
from google.colab import drive
drive.mount('/content/drive')

#@title <font size="5">← ឵឵<i>Install FFmpeg v4.2.2</font> { vertical-output: true }
from IPython.display import clear_output
import os, urllib.request
HOME = os.path.expanduser("~")
pathDoneCMD = f'{HOME}/doneCMD.sh'
if not os.path.exists(f"{HOME}/.ipython/ttmg.py"):
    hCode = "https://raw.githubusercontent.com/yunooooo/gcct/master/res/ttmg.py"
    urllib.request.urlretrieve(hCode, f"{HOME}/.ipython/ttmg.py")

from ttmg import (
    loadingAn,
    textAn,
)

loadingAn(name="lds")
textAn("Installing Dependencies...", ty='twg')
os.system('pip install git+git://github.com/AWConant/jikanpy.git')
os.system('add-apt-repository -y ppa:jonathonf/ffmpeg-4')
os.system('apt-get update')
os.system('apt install mediainfo')
os.system('apt-get install ffmpeg')
clear_output()
print('Installation finished.')

#@markdown <h3><b>FFMPEG Encode x265 10bit :</h3>

import os, sys, re

input_folder= '' #@param {type:"string"}
output_folder= '' #@param {type:"string"}
#@markdown <h3><b>Choose your encode setting :</h5>
#@markdown <h><i>main = default | main10 = HEVC 10 Bit</i>
encode_setting = "X265 AAC 1080p" #@param ["X265 AAC 720p", "X265 AAC 540p", "X265 Copy", "X265 AAC 1080p", "X265 AAC 480p"]
output_file_type = 'mkv' #@param ["mkv", "mp4"]
#@markdown <h3><b>Video quality :</h3>
#@markdown <h><i>0 (Best) to 51 (Worst)</i><h>
set_crf ='24.2'#@param {type:"string"}
set_audio ='0:1' #@param {type:"string"}
set_audio1 ='0:2' #@param {type:"string"}
my_suffixes = (".mp4", ".mov", ".mkv", ".avi", ".ts", ".flv", ".webm", ".wmv", ".mpg", ".m4v", ".f4v", ".m2ts", ".mpeg", ".3gp", ".MP4", ".MOV", ".MKV", ".AVI", ".TS", ".FLV", ".WEBM", ".WMV", ".MPG", ".M4V", ".F4V", ".M2TS", ".MPEG", ".3GP")

from pathlib import Path
Path(output_folder).mkdir(parents=True, exist_ok=True)

if encode_setting == 'X265 AAC 720p':
 for filename in os.listdir(input_folder):
    if (filename.endswith(my_suffixes)):
        cmd = !ffmpeg -stats  -i "$input_folder/{filename}" -metadata comment="X265-CRF$set_crf-AAC" -c:v libx265 -color_primaries 1 -color_range 1 -color_trc 1 -colorspace 1 -profile:v main10 -pix_fmt yuv420p10le -vf smartblur=1.5:-0.35:-3.5:0.65:0.25:2.0,scale=1280:720:spline16+accurate_rnd+full_chroma_int -preset medium  -x265-params me=2:rd=4:subme=7:aq-mode=3:aq-strength=1:deblock=1,1:psy-rd=1:psy-rdoq=1:rdoq-level=2:merange=57:bframes=8:b-adapt=2:limit-sao=1:frame-threads=3:no-info=1 -crf $set_crf -map 0:0 -map $set_audio -map $set_audio1 -map 0:s -c:a aac -b:a 160k -metadata title="Encoded By Ani Animesh" -metadata:s:0 title="Presented By Sakura Anime" -metadata:s:a:0 title="Ani Animesh" -metadata:s:a:1 title="Sakura Anime" -metadata:s:s:0 title="Sakura Anime" -metadata:s:s:1 title="@Animesh20"  "$output_folder/{filename.rpartition('.')[0]}.$output_file_type"

if encode_setting == 'X265 AAC 540p':
 for filename in os.listdir(input_folder):
    if (filename.endswith(my_suffixes)):
        cmd = !ffmpeg -stats -i "$input_folder/{filename}" -metadata comment="X265-CRF$set_crf-AAC" -c:v libx265 -color_primaries 1 -color_range 1 -color_trc 1 -colorspace 1 -profile:v main10 -pix_fmt yuv420p10le -preset medium -vf smartblur=1.5:-0.35:-3.5:0.65:0.25:2.0,scale=960:540:spline16+accurate_rnd+full_chroma_int -x265-params me=2:rd=4:subme=7:aq-mode=3:aq-strength=1:deblock=1,1:psy-rd=1:psy-rdoq=1:rdoq-level=2:merange=57:bframes=8:b-adapt=2:limit-sao=1:frame-threads=3:no-info=1 -crf $set_crf -map 0:0 -map $set_audio -map $set_audio1 -map 0:s -c:a aac -b:a 128k -metadata title="Encoded By Ani Animesh" -metadata:s:0 title="Presented By Sakura Anime" -metadata:s:a:0 title="Ani Animesh" -metadata:s:a:1 title="Sakura Anime" -metadata:s:s:0 title="Sakura Anime" -metadata:s:s:1 title="@Animesh20" -metadata:s:s:2 title="@AnimeChannelSakura"  "$output_folder/{filename.rpartition('.')[0]}.$output_file_type"

if encode_setting == 'X265 Copy':
 for filename in os.listdir(input_folder):
    if (filename.endswith(my_suffixes)):
        cmd = !ffmpeg -stats -i "$input_folder/{filename}" -metadata comment="X265-CRF$set_crf-AAC" -metadata title="Encoded By Ani Animesh" -metadata:s:0 title="Presented By Sakura Anime" -metadata:s:a:0 title="Ani Animesh" -metadata:s:a:1 title="Sakura Anime" -metadata:s:s:0 title="Sakura Anime" -metadata:s:s:1 title="@Animesh20" -metadata:s:s:2 title="@AnimeChannelSakura" -map 0 -codec copy "$output_folder/{filename.rpartition('.')[0]}.$output_file_type"

if encode_setting == 'X265 AAC 1080p':
 for filename in os.listdir(input_folder):
    if (filename.endswith(my_suffixes)):
        cmd = !ffmpeg -stats -i "$input_folder/{filename}" -metadata comment="X265-CRF$set_crf-AAC" -c:v libx265 -color_primaries 1 -color_range 1 -color_trc 1 -colorspace 1 -profile:v main10 -pix_fmt yuv420p10le -preset medium -vf smartblur=1.5:-0.35:-3.5:0.65:0.25:2.0,scale=1920:1080:spline16+accurate_rnd+full_chroma_int -crf $set_crf -map 0:0 -map $set_audio -map $set_audio1 -map 0:s -c:a aac -b:a 192k -metadata title="Encoded By Ani Animesh" -metadata:s:0 title="Presented By Sakura Anime" -metadata:s:a:0 title="Ani Animesh" -metadata:s:a:1 title="Sakura Anime" -metadata:s:s:0 title="Sakura Anime" -metadata:s:s:1 title="@Animesh20" -metadata:s:s:2 title="@AnimeChannelSakura" "$output_folder/{filename.rpartition('.')[0]}.$output_file_type"

if encode_setting == 'X265 AAC 480p':
  for filename in os.listdir(input_folder):
    if (filename.endswith(my_suffixes)):
      cmd = !ffmpeg -stats -i "$input_folder/{filename}" -metadata comment="X265-CRF$set_crf-AAC" -c:v libx265 -color_primaries 1 -color_range 1 -color_trc 1 -colorspace 1 -profile:v main10 -pix_fmt yuv420p10le -vf smartblur=1.5:-0.35:-3.5:0.65:0.25:2.0,scale=854:480:spline16+accurate_rnd+full_chroma_int -preset medium  -x265-params me=2:rd=4:subme=7:aq-mode=3:aq-strength=1:deblock=1,1:psy-rd=1:psy-rdoq=1:rdoq-level=2:merange=57:bframes=8:b-adapt=2:limit-sao=1:frame-threads=3:no-info=1 -crf $set_crf -map 0:0 -map $set_audio -map $set_audio1 -map 0:s -c:a aac -b:a 96k -metadata title="Encoded By Ani Animesh" -metadata:s:0 title="Presented By Sakura Anime" -metadata:s:a:0 title="Ani Animesh" -metadata:s:a:1 title="Sakura Anime" -metadata:s:s:0 title="Sakura Anime" -metadata:s:s:1 title="@Animesh20" -metadata:s:s:2 title="@AnimeChannelSakura"  "$output_folder/{filename.rpartition('.')[0]}.$output_file_type"

#@markdown <h3><b>FFMPEG Encode x264 10bit :</h3>

import os, sys, re

input_folder= '' #@param {type:"string"}
output_folder= '' #@param {type:"string"}
#@markdown <h3><b>Choose your encode setting :</h5>
#@markdown <h><i>main = default | main10 = HEVC 10 Bit</i>
encode_setting = "X264 AAC 480p" #@param ["X264 AAC 720p", "X264 AAC 540p", "X265 Copy", "X264 AAC 1080p", "X264 AAC 480p"]
output_file_type = 'mkv' #@param ["mkv", "mp4"]
#@markdown <h3><b>Video quality :</h3>
#@markdown <h><i>0 (Best) to 51 (Worst)</i><h>
set_crf ='24.2'#@param {type:"string"}
set_audio ='0:1' #@param {type:"string"}
set_audio1 ='0:2' #@param {type:"string"}
my_suffixes = (".mp4", ".mov", ".mkv", ".avi", ".ts", ".flv", ".webm", ".wmv", ".mpg", ".m4v", ".f4v", ".m2ts", ".mpeg", ".3gp", ".MP4", ".MOV", ".MKV", ".AVI", ".TS", ".FLV", ".WEBM", ".WMV", ".MPG", ".M4V", ".F4V", ".M2TS", ".MPEG", ".3GP")

from pathlib import Path
Path(output_folder).mkdir(parents=True, exist_ok=True)

if encode_setting == 'X264 AAC 720p':
 for filename in os.listdir(input_folder):
    if (filename.endswith(my_suffixes)):
        cmd = !ffmpeg -stats  -i "$input_folder/{filename}" -metadata comment="X265-CRF$set_crf-AAC" -c:v libx264 -color_primaries 1 -color_range 1 -color_trc 1 -colorspace 1 -profile:v high10 -pix_fmt yuv420p10le -vf smartblur=1.5:-0.35:-3.5:0.65:0.25:2.0,scale=1280:720:spline16+accurate_rnd+full_chroma_int -preset medium  -crf $set_crf -map 0:0 -map $set_audio -map $set_audio1 -map 0:s -c:a aac -b:a 160k -metadata title="Encoded By Ani Animesh" -metadata:s:0 title="Presented By Sakura Anime" -metadata:s:a:0 title="Ani Animesh" -metadata:s:a:1 title="Sakura Anime" -metadata:s:s:0 title="Sakura Anime" -metadata:s:s:1 title="@Animesh20"  "$output_folder/{filename.rpartition('.')[0]}.$output_file_type"

if encode_setting == 'X264 AAC 540p':
 for filename in os.listdir(input_folder):
    if (filename.endswith(my_suffixes)):
        cmd = !ffmpeg -stats -i "$input_folder/{filename}" -metadata comment="X265-CRF$set_crf-AAC" -c:v libx264 -color_primaries 1 -color_range 1 -color_trc 1 -colorspace 1 -profile:v high0 -pix_fmt yuv420p10le -preset medium -vf smartblur=1.5:-0.35:-3.5:0.65:0.25:2.0,scale=960:540:spline16+accurate_rnd+full_chroma_int -crf $set_crf -map 0:0 -map $set_audio -map $set_audio1 -map 0:s -c:a aac -b:a 128k -metadata title="Encoded By Ani Animesh" -metadata:s:0 title="Presented By Sakura Anime" -metadata:s:a:0 title="Ani Animesh" -metadata:s:a:1 title="Sakura Anime" -metadata:s:s:0 title="Sakura Anime" -metadata:s:s:1 title="@Animesh20" -metadata:s:s:2 title="@AnimeChannelSakura"  "$output_folder/{filename.rpartition('.')[0]}.$output_file_type"

if encode_setting == 'X265 Copy':
 for filename in os.listdir(input_folder):
    if (filename.endswith(my_suffixes)):
        cmd = !ffmpeg -stats -i "$input_folder/{filename}" -metadata comment="X265-CRF$set_crf-AAC" -metadata title="Encoded By Ani Animesh" -metadata:s:0 title="Presented By Sakura Anime" -metadata:s:a:0 title="Ani Animesh" -metadata:s:a:1 title="Sakura Anime" -metadata:s:s:0 title="Sakura Anime" -metadata:s:s:1 title="@Animesh20" -metadata:s:s:2 title="@AnimeChannelSakura" -map 0 -codec copy "$output_folder/{filename.rpartition('.')[0]}.$output_file_type"

if encode_setting == 'X264 AAC 1080p':
 for filename in os.listdir(input_folder):
    if (filename.endswith(my_suffixes)):
        cmd = !ffmpeg -stats -i "$input_folder/{filename}" -metadata comment="X265-CRF$set_crf-AAC" -c:v libx264 -color_primaries 1 -color_range 1 -color_trc 1 -colorspace 1 -profile:v high10 -pix_fmt yuv420p10le -preset medium -vf smartblur=1.5:-0.35:-3.5:0.65:0.25:2.0,scale=1920:1080:spline16+accurate_rnd+full_chroma_int -crf $set_crf -map 0:0 -map $set_audio -map $set_audio1 -map 0:s -c:a aac -b:a 192k -metadata title="Encoded By Ani Animesh" -metadata:s:0 title="Presented By Sakura Anime" -metadata:s:a:0 title="Ani Animesh" -metadata:s:a:1 title="Sakura Anime" -metadata:s:s:0 title="Sakura Anime" -metadata:s:s:1 title="@Animesh20" -metadata:s:s:2 title="@AnimeChannelSakura" "$output_folder/{filename.rpartition('.')[0]}.$output_file_type"

if encode_setting == 'X264 AAC 480p':
  for filename in os.listdir(input_folder):
    if (filename.endswith(my_suffixes)):
      cmd = !ffmpeg -stats -i "$input_folder/{filename}" -metadata comment="X265-CRF$set_crf-AAC" -c:v libx264 -color_primaries 1 -color_range 1 -color_trc 1 -colorspace 1 -profile:v high10 -pix_fmt yuv420p10le -tune animation -vf smartblur=1.5:-0.35:-3.5:0.65:0.25:2.0,scale=854:480:spline16+accurate_rnd+full_chroma_int -preset medium -crf $set_crf -map 0:0 -map $set_audio -map $set_audio1 -map 0:s -c:a aac -b:a 96k -metadata title="Encoded By Ani Animesh" -metadata:s:0 title="Presented By Sakura Anime" -metadata:s:a:0 title="Ani Animesh" -metadata:s:a:1 title="Sakura Anime" -metadata:s:s:0 title="Sakura Anime" -metadata:s:s:1 title="@Animesh20" -metadata:s:s:2 title="@AnimeChannelSakura"  "$output_folder/{filename.rpartition('.')[0]}.$output_file_type"

"""# <center>***HandBrake*** </center> 
# <Center> <img src="https://handbrake.fr/img/logo.png" width="40"></center>
"""

# Commented out IPython magic to ensure Python compatibility.
# #@title <<----<strong>Install HandBrake and rClone</strong>
# %%capture
# AUTO_RECONNECT = True #@param {type:"boolean"}
# HANDBRAKE = True #@param {type:"boolean"}
# RCLONE = True #@param {type:"boolean"}
# #@markdown Check AUTO_RECONNECT to prevent notebook from disconnecting!
# 
# from os import makedirs
# makedirs("/content/temp/HandbrakeTemp", exist_ok = True)
# makedirs("/root/.config/rclone", exist_ok = True) 
# if HANDBRAKE==True:
#   !wget -qq https://github.com/vot/ffbinaries-prebuilt/releases/download/v4.2.1/ffmpeg-4.2.1-linux-64.zip 
#   !rm -f ffmpeg-4.2.1-linux-64.zip
#   !add-apt-repository ppa:stebbins/handbrake-releases -y 
#   !apt-get install -y handbrake-cli 
#   
# if RCLONE==True:
#   !curl https://rclone.org/install.sh | sudo bash
# 
# if AUTO_RECONNECT:
#   import IPython
#   from google.colab import output
# 
#   display(IPython.display.Javascript('''
#   function ClickConnect(){
#     btn = document.querySelector("colab-connect-button")
#     if (btn != null){
#       console.log("Click colab-connect-button"); 
#       btn.click() 
#       }
#     
#     btn = document.getElementById('ok')
#     if (btn != null){
#       console.log("Click reconnect"); 
#       btn.click() 
#       }
#     }
#     
#   setInterval(ClickConnect,60000)
#   '''))

#@title <center> HandBrake Configuration </center>
#@markdown > Select Mode ( Batch conversion/ Single File)
MODE = "SINGLE" #@param ["SINGLE", "BATCH"]


#@markdown ---
SOURCE = "" #@param {type:"string"}
DESTINATION = "" #@param {type:"string"}
FORMAT = "mkv" #@param ["mp4", "mkv"]
RESOLUTION = "720p" #@param ["360p", "480p","540p", "720p", "1080p"]
Encoder = "x265_10bit" #@param ["x264_10bit", "x265_10bit"]
Encoder_Preset = "medium" #@param ["ultrafast", "faster", "fast", "medium", "slow", "slower"]
#@markdown Choose Constant Quality Rate [Lower = Higher Quality/
#@markdown Larger File Size]
CQ = 24.2 #@param {type:"slider", min:10, max:30, step:1}
BURN_SUBTITLES = False #@param {type:"boolean"}
Additional_Flags = "" #@param {type:"string"}
#@markdown ---
Email_Alert = False #@param {type:"boolean"}
MESSAGE = "HandBrakeCLI_Colab has finished working" #@param ["HandBrake has finished working"] {allow-input: true}
SENDER_ID ="" #@param {type:"string"}
SENDER_PASS="" #@param {type:"string"}
RECEIVER_ID="" #@param {type:"string"}
#@markdown >#####  Using an app specific password is recommended: https://myaccount.google.com/apppasswords

########################################################
import smtplib
import os


formats = ('.mkv','.mp4','.ts','.avi','.mov','.wmv')

######## Renames the file ########
def fileName(fPath):
        tName = fPath.split('/')[-1]        
        if tName.endswith('ts'):
          tName = '[HANDY] ' + tName[:-3] + f' [{RESOLUTION}] [{Encoder}].{FORMAT}'    
        else:
          tName = '[HANDY] ' + tName[:-4] + f' [{RESOLUTION}] [{Encoder}].{FORMAT}'    
        return tName

def set_resolution():
  global w,h,flags
  if RESOLUTION == "360p":
    w, h = "480" , "360"
  elif RESOLUTION == "480p":
    w, h = "854" , "480"
  elif RESOLUTION == "540p":
    w, h = "960" , "540"
  elif RESOLUTION == "720p":
    w, h = "1280" , "720"
  elif RESOLUTION == "1080p":
    w, h = "1920" , "1080"

def addFlags():
  global flags
  flags = f" --encoder {Encoder}  --all-audio -s '0,1,2,3' --cfr --optimize --quality={CQ} --width={w} --height={h} --format={FORMAT} --encoder-preset={Encoder_Preset} "
  if BURN_SUBTITLES:
    flags += "-s '1' --subtitle-burned '1' "
  if Additional_Flags != "":
    flags += str(Additional_Flags)

set_resolution()
addFlags()

##### HandBrake and Rclone #####
def runner(path):
  f_name = fileName(path)
  hTemp=f"/content/temp/HandbrakeTemp/{f_name}"
  !HandBrakeCLI -i "$path" -o "$hTemp" $flags
  
      
  if os.path.isfile(hTemp):
    print(f"\n\n********** Successfully converted {f_name}\n Now saving to Destination.....")
    if os.path.exists('/usr/bin/rclone'):
      !rclone move "$hTemp" --user-agent "Mozilla" "$DESTINATION" --transfers 20 --checkers 20 --stats-one-line --stats=5s -v --tpslimit 95 --tpslimit-burst 40
    else:
      dest = DESTINATION+'/'+f_name
      !mv "$hTemp" "$dest"
  if os.path.isfile(DESTINATION+ '/' +f_name):    
      print(f"\n\n********** Successfully saved {f_name} to Destination")

########## Check Mode ########
if MODE=="BATCH":
  os.makedirs(DESTINATION, exist_ok=True)
  if SOURCE.endswith('/'):
      pass
  else: SOURCE +='/'
  filesList = os.listdir(SOURCE+'.')
  if os.path.isfile(SOURCE+'processed_db.txt'):
    pass
  else:
    with open((SOURCE+'processed_db.txt'), 'w') as fb:
      fb.write("Do not delete this file until all files have been processed!\n")
      fb.close()
  with open((SOURCE+'processed_db.txt'), "r+") as filehandle:
    processedList = [x.rstrip() for x in filehandle.readlines()]

    print('<<<<<<<<<<<<<<<<<< Starting Conversion in Batch mode. >>>>>>>>>>>>>>>>>>')

    for currentFile in filesList:
      if currentFile.endswith(formats):
        if currentFile not in processedList:
          currentPath = SOURCE + currentFile      
          print(f'\n\n**************** Current File to process: {currentFile}')
          runner(currentPath)
          filehandle.write(currentFile+'\n')
    filehandle.close()
        

else:
    if SOURCE.endswith(formats):    
        runner(SOURCE)
    else: print("Are you sure you have selected the correct file??")

########### Sending Notification ###############
if Email_Alert == True: 
  from email.mime.multipart import MIMEMultipart 
  from email.mime.text import MIMEText 
  msg = MIMEMultipart()
  msg['From'] = SENDER_ID
  msg['To'] = RECEIVER_ID
  msg['Subject'] = "HandBrakeCLI_Colab has finished executing!" 
  
  msg.attach(MIMEText(MESSAGE))
  s = smtplib.SMTP('smtp.gmail.com', 587) 
  s.starttls() 
  s.login(SENDER_ID, SENDER_PASS)
  s.sendmail(SENDER_ID, RECEIVER_ID, msg.as_string())
  print("Email Alert Sent!")  
  s.quit()
