import subprocess

subprocess.call(['ls', '-1'], shell=True)

subprocess.call('echo $HOME', shell=True)

subprocess.check_call(['true'])

#subprocess.check_call(['false'])

output = subprocess.check_output(['ls', '-1'])
print ('Have %d bytes in output' % len(output))
print (output)


output = subprocess.check_output(
    'echo to stdout; echo to stderr 1>&2; exit 1',
    shell=True,
    )
print ('Have %d bytes in output' % len(output))
print (output)

