$(function() {
$("#error_msg").hide()
$(".inputform").on("mouseenter", ".courseInput", function() {
    if ($(this).attr("valid") == "false") {
        var offset = $(this).offset()
        offset.top = offset.top + $(this).outerHeight()
        $("#error_msg").css("display", "block")
        $("#error_msg").offset(offset)
        $("#error_msg").css("width", $(this).css("width"))
        $("#error_msg").text(GetErrorMessage($(this).val()))
    }
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
    RefreshInputs()
})
.on("focus", ".courseInput", function() {
    $(".courseInput").autocomplete(
        {source: courseData}) 
})
.on("click", ".courseInputRemove", function() {
    $(this).parent().remove()
    RefreshInputs()
})
$(".addInputButton").click(function() {
    var newInput = "<div class='courseInputWrapper'><a href='javascript:;' class='courseInputRemove'><img src='image/remove.png' class='remove_button'></a><input class='courseInput'>"
    $(this).parent().find("form").append(newInput)  
})
function RefreshInputs(){
    var curData = []
    $(".courseInput").each(function(){
        if ($(this).val() != '') {
            var tempdata = {course:$(this).val(), semester:$(this).parent().parent().attr("semester")}
            curData.push(tempdata)
        }
    })
    ValidateAllInput(curData)
    $(".courseInput").each(function() {
        if (IsValid($(this).val())) {
            $(this).attr("valid", "true")
            console.log("true" + $(this).val())
        } else {
            $(this).attr("valid", "false")
            console.log("false" + $(this).val())
        }
    })
}

var apForm,
apForm = $("#ap_form").dialog({
    autoOpen: false,
    height:300,
    width:350,
    modal: true,
    close: function() {
        RefreshInputs()
    }
})
$("#ap_form_button").button().on("click", function(){
    apForm.dialog("open")
})
$("#ap_form").on("click", ".addApSelectButton", function() {
    var newInput = "<div class='apInputWrapper'><a href='javascript:;' class='apInputRemove'><img src='image/remove.png' class='ap_remove_button'></a>"
    newInput += "<label>Course</label>"
    newInput += "<select class='apCourseSelect' name=''>"
    for (ap of apData) {
        newInput += "<option>"
        newInput += ap.label
        newInput += "</option>"
    }
    newInput += "</select>"
    newInput += "<label>Score</label>"
    newInput += "<select class='apScoreSelect'><option>3</option><option>4</option><option>5</option></select>"
    newInput += "</div>"
    console.log(newInput)
    $(this).parent().find("form").append(newInput) 
})
.on("click", ".apInputRemove", function(){
    $(this).parent().remove()
})
})