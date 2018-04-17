$(document).ready(function(){

    //Student Login
    $("#stdnt_logn_form").submit(function(e){
        var name = $("#stdnt_logn_name").val();
        var roll_no = $("#stdnt_logn_rollno").val();
//         e.PreventDefault();
//         alert(name + roll_no);
        if(name == ''){
            e.preventDefault();
            $("#stdnt_logn_form_error").addClass("alert alert-danger").text("Please enter your name");
        }
        else if(roll_no == ''){
            e.preventDefault();
            $("#stdnt_logn_form_error").addClass("alert alert-danger").text("Please enter your roll no.");
        }
    });

    $(".add_new_student").click(function(){
        $(".add_new_student_frm").toggle('slow');
    });

    $("#send_new_msg_btn").click(function(){
        $("#send_new_msg_div").toggle('slow');
    });

    $('.add_student_attendance').click(function(){
      if ($(this).find('.add_student_ckbx').is(':checked')) {
        $(this).children('span').html('Present').css('background-color', '#a3e4a3');
      }
      else{
        $(this).children('span').html('Absent').css('background-color', '#fff');;
      }
    });

    $('#select_all_studnts').change(function(){
        // alert('wrkng');
        if($(this).find('input').is(':checked')){
            // alert('true');
            $('input[name="send_message[]"]').each(function(){
                $(this).prop('checked', true);
            });
        }
        else{
            $('input[name="send_message[]"]').each(function(){
                $(this).prop('checked', false);
            });
        }
    });
});