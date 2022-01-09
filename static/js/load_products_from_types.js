const typeInput = document.getElementById("product_type")
var productInput = document.getElementById("product_name")

typeInput.addEventListener('change', e=>{
    const selectedType = e.target.value
    $.ajax({
        type: 'GET',
        url: `product-json/${selectedType}/`,
        success: function(response){
            const productData = response.data
            productInput.options.length = 0;
            productData.map(i=>{
                var opt = document.createElement('option')
                opt.text = i.name
                opt.value = i.name
                productInput.appendChild(opt)
            })
        },
        error: function(error){
            console.log(error)
        }
    })
})

            
