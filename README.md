# rotationstagecontrol


## Powershell test


```
$udpClient = New-Object System.Net.Sockets.UdpClient
$message = [System.Text.Encoding]::ASCII.GetBytes("Your message here")
$udpClient.Send($message, $message.Length, "<localhost>", <5005>)
```
