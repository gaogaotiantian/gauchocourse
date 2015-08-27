$(function() {
$("#error_msg").hide()
$(".inputform").on("mouseenter", ".courseInput", function() {
    var offset = $(this).offset()
    offset.top = offset.top + $(this).outerHeight()
    $("#error_msg").css("display", "block")
    $("#error_msg").offset(offset)
    
})
.on("mouseleave", ".courseInput", function() {
    $("#error_msg").css("display", "none")
})
.on("blur", ".courseInput", function() {
    if ($(this).val() == "") {
        $(this).attr("valid", "na")
    } else {
        $(this).attr("valid", "true")
    }
    ValidateAllInput()

})
.on("focus", ".courseInput", function() {
    $(".courseInput").autocomplete(
        {source: courseData}) 
})
.on("click", ".courseInputRemove", function() {
    $(this).parent().remove()
})
$(".addInputButton").click(function() {
    var newInput = "<div class='courseInputWrapper'><button class='courseInputRemove'><img src=minus.png class=minus></button><input class='courseInput'>"
    $(this).parent().find("form").append(newInput)  
})
function ValidateAllInput(){
    var data = []
    $(".courseInput").each(function(){
        if ($(this).val() != '') {
            var tempdata = {course:$(this).val(), semester:$(this).parent().parent().attr("semester")}
            data.push(tempdata)
        }
    })
    console.log(data)
}
})

/*
$(function() {
$(".courseInput").blur(function() {
    if ($(this).val() == "") {
        $(this).attr("valid", "na")
    } else {
        $(this).attr("valid", "true")
    }
    ValidateAllInput()
})

$("#error_msg").hide()
$(".courseInput").mouseenter(function() {
    var groupName = $(this).attr("group")
    //$(".error").each(function(){
    //    if ($(this).attr("group") == groupName) {
    //        $(this).toggle()
    //        $(this).css("margin-bottom", -$(this).height())
    //    }
    //})
    var offset = $(this).offset()
    offset.top = offset.top + $(this).outerHeight()
    $("#error_msg").css("display", "block")
    $("#error_msg").offset(offset)
    
})
.mouseleave(function() {
    $("#error_msg").css("display", "none")
})
function ValidateAllInput(){
    var data = []
    $(".courseInput").each(function(){
        if ($(this).val() != '') {
            var tempdata = {course:$(this).val(), semester:$(this).parent().attr("semester")}
            data.push(tempdata)
        }
    })
    console.log(data)
}
})
*/