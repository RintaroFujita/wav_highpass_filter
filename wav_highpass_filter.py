!pip install pydub
from google.colab import drive
drive.mount('/content/drive')
from pydub import AudioSegment
import os

# Google Drive内のディレクトリパスを指定
input_directory = "/content/drive/MyDrive/siri_tenji"
output_directory = "/content/drive/MyDrive/siri_tenji/highpas_tenji"

# 出力ディレクトリが存在しない場合は作成する
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# ハイパスフィルターのカットオフ周波数を設定 (Hz)
cutoff_frequency = 1000

# ゲインを設定 (dB)：正の値で音量が上がり、負の値で音量が下がります
gain = 10  # 6 dBのゲインを追加

# Google Drive内の音声ファイルを取得
input_files = [f for f in os.listdir(input_directory) if f.endswith(".wav")]

# 各音声ファイルに対して処理を行う
for input_file in input_files:
    # 入力ファイルのパス
    input_path = os.path.join(input_directory, input_file)

    # 出力ファイルのパスを生成 (拡張子は変更しない)
    output_file = os.path.splitext(input_file)[0] + "_highpass.wav"
    output_path = os.path.join(output_directory, output_file)

    # 音声ファイルを読み込む
    audio = AudioSegment.from_wav(input_path)

    # ハイパスフィルターを適用
    filtered_audio = audio.high_pass_filter(cutoff_frequency)

    # ゲインを適用
    filtered_audio = filtered_audio + gain

    # ステレオ音声をモノラルに変換
    filtered_audio = filtered_audio.set_channels(1)

    # フィルター、ゲイン処理、モノラル化後の音声を保存
    filtered_audio.export(output_path, format="wav")

print("処理が完了しました。")
