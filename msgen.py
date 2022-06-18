import random, keyboard, time, os, json


def gen_end_seq():
    sequence = r'!@#$%^&*()_+-=[]\;/.,{}|:"<>?"'
    char = random.choice(sequence)
    end_seq = char
    end_count = 30
    while end_count > 0:
        end_seq += char
        end_count -= 1
    return end_seq

def gen_lbad(jsdict):
    purse = jsdict["lbad"]["purse"]
    msg = "LOWBALLING w/ "+purse+"M PURSE (NO non-auctionable, skins, furniture) /visit zrns"
    return msg

def gen_lflb(jsdict):
    itype = jsdict["lflb"]["type"]
    items = jsdict["lflb"]["items"]
    msg = "LOOKING FOR "+itype.upper()+" LOWBALLER to buy MY "+items+" /p zrns or /visit zrns"
    return msg

def gen_ahad(jsdict):
    items = jsdict["ahad"]["items"]
    msg = "LOWEST BINs ["+items+"] /ah zrns"
    return msg

def gen_lfku(jsdict):
    tier = jsdict["lfku"]["tier"]
    pcount = jsdict["lfku"]["pcount"]
    notes = jsdict["lfku"]["notes"]
    msg = pcount+'/4 T'+tier+' KUUDRA '+notes+' /p zrns'
    return msg

def gen_lfgku(jsdict):
    tier = jsdict["lfgku"]["tier"]
    build = jsdict["lfgku"]["build"]
    msg = "LF KUUDRA T"+tier+' PARTY, AM '+build+' /p zrns'
    return msg

def crimson_spam(iterator, mod, jsdict):
    if iterator == 1:
        enter_msg('/warp crimson', False, False)
        iterator += 1
    elif iterator == 2:
        if mod == 'lfku':
            enter_msg(gen_lfku(jsdict), True, True)
        elif mod == 'lfgku':
            enter_msg(gen_lfgku(jsdict), True, True)
        iterator += 1
    elif iterator == 3:
        enter_msg('/is', False, False)
        iterator = 1
    return iterator

def enter_msg(msg, endb, ac):
    if endb:
        end = gen_end_seq()
        msg += ' '+end
    if ac:
        ac = "/ac "
        msg = ac + msg
    keyboard.send('t')
    time.sleep(0.1)
    keyboard.write(msg)
    time.sleep(0.1)
    keyboard.send('enter')

def read_json_file():
    json_file = open('chat_var.json')
    addict = json.load(json_file)
    json_file.close()
    return addict

def write_to_json(jsdict):
    outfile = open('chat_var.json', 'w')
    json.dump(jsdict, outfile)
    outfile.close()

def main():
    os.chdir(r'folder')
    mod = input('mod?: ')
    iterator = 1
    print('- to select mod = to run mod')
    while True:
        if keyboard.is_pressed('-'):
            keyboard.send('alt+tab')
            jsdict = read_json_file()
            keylist = ''
            keys = jsdict.keys()
            for key in keys:
                keylist += key
                keylist += ', '
            print(keylist)
            print('space at end for options')
            mod = input('mod?: ')
            print('mod changed to: '+mod)
            if mod[-1] == ' ':
                mod = mod[:-1]
                print(jsdict[mod])
                to_edit = input('which element to edit?: ')
                change_to = input('change to?: ')
                jsdict[mod][to_edit] = change_to
                print(to_edit+' changed to '+change_to)
                write_to_json(jsdict)
            print('current mod: '+mod)
        if keyboard.is_pressed('='):
            jsdict = read_json_file()
            if mod == 'lbad':
                enter_msg(gen_lbad(jsdict), True, True)
            elif mod == 'lflb':
                enter_msg(gen_lflb(jsdict), True, True)
            elif mod == 'ahad':
                enter_msg(gen_ahad(jsdict), True, True)
            elif mod == 'lfku':
                iterator = crimson_spam(iterator, mod, jsdict)
            elif mod == 'lfgku':
                iterator = crimson_spam(iterator, mod, jsdict)
if __name__ == "__main__":
    main()
