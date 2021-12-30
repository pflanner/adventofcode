from util import get_lines_for_day


def f(lines):
    message = ''.join(lines)
    prev_message = ''

    while message.find('(') != -1 and message != prev_message:
        i = 0
        uncompressed = []
        while i < len(message):
            marker_start = message.find('(', i)

            if marker_start != -1:
                uncompressed.append(message[i:marker_start])
                marker_end = message.find(')', marker_start)
                marker = message[marker_start + 1:marker_end]
                marker = marker.split('x')
                section_len = int(marker[0])
                repeat = int(marker[1])
                section_start = marker_end + 1
                section_end = section_start + section_len

                uncompressed.extend([message[section_start:section_end] * repeat])
                i = section_end
            else:
                uncompressed.append(message[i:])
                break

        prev_message = message
        message = ''.join(uncompressed)

    return len(message)


def g(lines):
    message = ''.join(lines)

    def dfs(start=0, end=len(message), multiplier=1):
        if message[start:end].find('(') == -1:
            return (end - start) * multiplier

        marker_start = message.find('(', start)
        marker_end = message.find(')', marker_start)
        marker = message[marker_start + 1:marker_end]
        marker = marker.split('x')
        section_len = int(marker[0])
        repeat = int(marker[1])
        section_start = marker_end + 1
        section_end = section_start + section_len

        return (marker_start - start + dfs(section_start, section_end, repeat) + dfs(section_end, end, 1)) * multiplier

    return dfs()


print(g(get_lines_for_day(2016, 9)))
# part 1
# 122797 is too high
