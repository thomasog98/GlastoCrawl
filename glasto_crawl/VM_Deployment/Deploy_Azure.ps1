# PowerShell script to create a virtual machine from a specified template in Azure

# Variables
$resourceGroupName = "RG_glastonbury_botnet"
$templateUri = "/home/thomas/glasto_template.json"
$vmName = "glastobot_"
$location = "UK South"

# Login to Azure
Connect-AzAccount

for ($i = 1; $i -le 2; $i++) {
    Write-Output "Number: $i"

$vmName = $vmName+$i
# Deploy VM from template
New-AzResourceGroupDeployment -ResourceGroupName $resourceGroupName -TemplateFile "" -TemplateParameterFile $templateUri -vmName $vmName

}