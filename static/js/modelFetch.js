function removeOptions(selectElement)
{
    console.log("Del");
    var i, L = selectElement.options.length - 1;

    for(i = L; i >= 0; i--) {
        selectElement.remove(i);
    }
}

async function setModels()
{
    var makeSelect = document.getElementById("makeSelect");
    var modelSelect = document.getElementById("modelSelect");

    removeOptions(modelSelect);
    modelSelect.add(new Option("Model", ""));

    if (makeSelect.value == "") return;

    var response = await fetch("/api/make/" + makeSelect.value);
    var models = JSON.parse(await response.json());

    if (typeof selectedModel != 'undefined')
        console.log(selectedModel);

    models.forEach(element => {
        if (typeof selectedModel != 'undefined')
        {
            if (selectedModel == element.fields.name)
            {
                modelSelect.add(new Option(element.fields.name, element.fields.name, false, true));
            }
            else
            {
                modelSelect.add(new Option(element.fields.name, element.fields.name));
            }
        }
        else
        {
            modelSelect.add(new Option(element.fields.name, element.fields.name));
        }
    });
}