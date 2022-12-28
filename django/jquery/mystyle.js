$('h1').click(function(){
    console.log("There was a click and change.")
    $(this).text("I was changed!!")
})

$('li').click(function(){
    console.log("There was click on li element.")
})