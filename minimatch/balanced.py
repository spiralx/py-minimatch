
from collections import namedtuple

Sub = namedtuple("Sub", "start start_delim end end_delim pre body post")


def balanced_match(start_delim, end_delim, s):
    sl = len(s)
    msl = len(start_delim)
    mel = len(end_delim)

    match = None
    depth = 0
    x = 0
    max_x = sl - msl - mel

    while x < max_x:
        if s[x: x + msl] == start_delim:
            if not match:
                match = Sub(x, start_delim, None, None, s[:x], None, None)
            x += msl
            depth += 1
            continue

        elif s[x: x + mel] == end_delim:
            depth -= 1

            if depth == 0:
                match.end = x
                match.end_delim = end_delim
                match.body = s[match.x + msl: x]
                match.post = s[x + mel:]
                return match

            x += mel
            continue

        x += 1

    if match:
        match.body = s[match.x + msl:]
        match.post = ""

    return match

"""
function balanced(a, b, str) {
  var bal = 0;
  var m = {};
  var ended = false;

  for (var i = 0; i < str.length; i++) {
    if (a == str.substr(i, a.length)) {
      if (!('start' in m)) m.start = i;
      bal++;
    }
    else if (b == str.substr(i, b.length) && 'start' in m) {
      ended = true;
      bal--;
      if (!bal) {
        m.end = i;
        m.pre = str.substr(0, m.start);
        m.body = (m.end - m.start > 1)
          ? str.substring(m.start + a.length, m.end)
          : '';
        m.post = str.slice(m.end + b.length);
        return m;
      }
    }
  }

  // if we opened more than we closed, find the one we closed
  if (bal && ended) {
    var start = m.start + a.length;
    m = balanced(a, b, str.substr(start));
    if (m) {
      m.start += start;
      m.end += start;
      m.pre = str.slice(0, start) + m.pre;
    }
    return m;
  }
}
"""
