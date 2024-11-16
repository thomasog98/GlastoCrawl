# PowerShell script to create a virtual machine from a specified template in Azure

# Variables
$resourceGroupName = "RG_glastonbury_botnet"
$template = "/home/thomas/template.json"
$templateParameters = "/home/thomas/parameters.json"
$vmName = "glastobot"
$location = "UK South"

# Login to Azure
Connect-AzAccount

for ($i = 1; $i -le 2; $i++) {
    Write-Output "Number: $i"

$vmName = $vmName+$i
# Deploy VM from template
New-AzResourceGroupDeployment -ResourceGroupName $resourceGroupName -TemplateFile $template -TemplateParameterFile $templateParameters -Name $vmName

}