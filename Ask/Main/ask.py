#!/usr/bin/env python

import main, time, subprocess, lib

logfile = open("server_log.tmp", "w")

subprocess.Popen("./runStanfordParserServer.sh", shell=True, stdout=logfile, stderr=logfile)

lib.pretty_print ("waiting for server")
time.sleep(30)
lib.pretty_print ("done!")

main.main()
