def change(music):
    music = music.replace("C#", "c")
    music = music.replace("D#", "d")
    music = music.replace("F#", "f")
    music = music.replace("G#", "g")
    music = music.replace("A#", "a")
    return music

def solution(m, musicinfos):
    answer = ''
    cnt, l = -1, 0
    m = change(m)
    for music in musicinfos:
        music = change(music)
        lst = music.split(',')
        tmp1, tmp2 = lst[0].split(':'), lst[1].split(':')
        st = int(tmp1[0]) * 60 + int(tmp1[1])
        ed = int(tmp2[0]) * 60 + int(tmp2[1])
        time = ed - st
        tmp = lst[3] * (time // len(lst[3])) + lst[3][:(time % len(lst[3]))]
        if m in tmp:
            if l < time:
                cnt = tmp.count(m)
                l = time
                answer = lst[2]
    if cnt == -1:
        return "(None)"
    else:
        return answer

# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("1111", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CDEFGAC", ["23:00,00:00,HELLO,CDEFGA"]))