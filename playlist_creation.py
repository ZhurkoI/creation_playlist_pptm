import os, shutil, itertools

# Initial data:
music_dir_init = r"e:\Music_PPTM\music_source"
music_dir_dest = r"e:\Music_PPTM\music_done"
ad_dir = r"e:\Music_PPTM\advertising"
delta_init = 5   # after this quantity of tracks the ad track will be inserted

music_files_list = os.listdir(music_dir_init)
ad_files_list = os.listdir(ad_dir)

N_music_tracks = len(music_files_list)
N_ad_tracks = len(ad_files_list)

N = 1
delta = delta_init
# delta_ad = N_ad_tracks
i_ad = 0
print("In progress...")
while music_files_list:

    N = str(N)
    src = os.path.join(music_dir_init, music_files_list[0])
    dst = os.path.join(music_dir_dest, N + ".mp3")  # добавляем расширение .mp3. Любое другое будет заменено на mp3
    # shutil.move(src, dst)  # переместит файлы
    shutil.copy2(src, dst)    # скопирует файлы
    N = int(N)
    music_files_list.pop(0)
    N += 1
    delta -= 1

    if delta == 0:
        src = os.path.join(ad_dir, ad_files_list[i_ad])
        dst = os.path.join(music_dir_dest, str(N) + ".mp3")
        shutil.copy2(src, dst)
        i_ad += 1
        N = int(N) + 1
        delta = delta_init

        if i_ad == N_ad_tracks:
            i_ad = 0

print("Done!")