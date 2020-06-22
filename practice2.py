#第一题
def match_ends(words):
    # +++your code here+++
    count = 0
    for item in words:
        item_list = list(item)
        if len(item_list)<2:
            continue
        if item_list[0] == item_list[len(item_list)-1]:
            count += 1
    return count
def test(got, expected):
    if got == expected:
        prefix = '正确!'
    else:
        prefix = '错误!'
    print('%s 你的结果: %s 应该返回的结果: %s' % (prefix, repr(got), repr(expected)))

#第二题
def front_x(words):
    list1 = []
    list2 = []
    for item in words:
        if item[0] == 'x':
            list1.append(item)
        else:
            list2.append(item)

    # +++your code here+++
    list1 = sorted(list1)
    list2 = sorted(list2)
    list1.extend(list2)
    return list1
#第三题
def sort_last(tuples):
    # +++your code here+++
    dict_ = {}
    dict_list = []
    for item in tuples:
        dict_[item[-1]] = item
    list_keys = dict_.keys()
    list_keys = sorted(list_keys)
    for i in list_keys:
        dict_list.append(dict_[i])

    return dict_list

#第四题
def remove_adjacent(nums):
    # +++your code here+++
    for i in range(len(nums)-1,0,-1):
        if nums[i] == nums[i-1]:
            del nums[i]
    return nums

#第五题
def linear_merge(list1, list2):
    # +++your code here+++
    list = []
    while len(list1) and len(list2):
        if list1[0] < list2[0]:
            list.append(list1.pop(0))
        else:
            list.append(list2.pop(0))
    list.extend(list1)
    list.extend(list2)
    return list
#第六题
def both_ends(s):
    # +++your code here+++
    if len(s) < 2:
        return ''
    elif len(s) == 2:
        return s
    else:
        return s[0:2] + s[len(s)-2:len(s)]
#7
def fix_start(s):
    # +++your code here+++
    return s[0] + s[1:len(s)].replace(s[0],'*')
#8
def mix_up(a, b):
    # +++your code here+++
    #1.使用空格把两个字符串分隔后合并成一个字符串
    #2.交换两个字符串的最前面的两个字母
    #3.字符串 a 和 b 的长度都大等于2
    if len(a)<3 or len(b)<3:
        return False
    return b[0:2] + a[2::] +' '+ a[0:2] + b[2::]

#9
def verbing(s):
    # +++your code here+++
    if len(s) >= 3:
        if 'ing' in s:
            s = s + 'ly'
        else:
            s = s + 'ing'
    return s
#10
def front_back(a, b):
    # +++your code here+++
    #判断长度奇数偶数
    len_a_2 = int(len(a)/2)
    len_b_2 = int(len(b)/2)

    if len(a)%2 == 1:
        if len(b)%2 == 1:
            return a[0:len_a_2+1]+b[0:len_b_2+1]+a[len_a_2+1:len(a)]+b[len_b_2+1:len(b)]
        else:
            return a[0:len_a_2+1]+b[0:len_b_2]+a[len_a_2+1:len(a)]+b[len_b_2:len(b)]
    else:
        if len(b)%2 == 1:
            return a[0:len_a_2]+b[0:len_b_2+1]+a[len_a_2:len(a)]+b[len_b_2+1:len(b)]
        else:
            return a[0:len_a_2]+b[0:len_b_2]+a[len_a_2:len(a)]+b[len_b_2:len(b)]
#last
import random
def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++
  # LAB(begin solution)
  mimic_dict = {}
  f = open(filename, 'r', encoding='utf-8')
  text = f.read()
  f.close()
  words = text.split()
  prev = ''
  for word in words:
    if not prev in mimic_dict:
      mimic_dict[prev] = [word]
    else:
      mimic_dict[prev].append(word)
    # Could write as: mimic_dict[prev] = mimic_dict.get(prev, []) + [word]
    # It's one line, but not totally satisfying.
    prev = word
  return mimic_dict

def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # +++your code here+++
  # LAB(begin solution)
  for unused_i in range(200):
    print(word,)
    nexts = mimic_dict.get(word)          # Returns None if not found
    if not nexts:
      nexts = mimic_dict['']  # Fallback to '' if not found
    word = random.choice(nexts)

def sort_last2(tuples):
  # return sorted(tuples, key=last)
  return sorted(tuples, key=lambda d: d[-1],reverse=True)
print(sort_last2([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))