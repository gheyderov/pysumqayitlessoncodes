window.addEventListener('load', async function(event){
    let response = await this.fetch('http://localhost:8000/api/categories/')
    let resDataCategories = await response.json()
    let recipeCategory = this.document.getElementById('recipe-category')
    for (category of resDataCategories){
        recipeCategory.innerHTML += `
             <option value="${category.id}">${category.title}</option>
        `
    }
    let responseTags = await this.fetch('http://localhost:8000/api/tags/')
    let resDataTags = await responseTags.json()
    let recipeTags = this.document.getElementById('recipe-tags')
    for (tag of resDataTags){
        recipeTags.innerHTML += `
             <option value="${tag.id}">${tag.title}</option>
        `
    }

})

let recipeCreationForm = document.querySelector('#recipe-creation-form')
recipeCreationForm.addEventListener('submit', async function(event){
    event.preventDefault()
    let formData = new FormData(recipeCreationForm)
    let responseForm  = await fetch('http://localhost:8000/api/recipes/', {
        method: 'POST',
        headers: {
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk0MTA1MzEwLCJpYXQiOjE2OTQxMDUwMTAsImp0aSI6ImI5OTk3MDYzNDM1MjQzYTFhMmI5MDM3ZmIzMjJkMzY0IiwidXNlcl9pZCI6MTZ9.cBRR0PTMH32yf2FxNNcsqqyGBt6KADAxSTId3a1WRxY'
        },
        body: formData
    })
    console.log(await responseForm.json())
})