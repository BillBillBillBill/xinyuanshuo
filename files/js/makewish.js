
  //获取当前时间
  function getFormatTime()
  {
    function addzero(t){return t<10?'0'+t:t;};
    var time = new Date();
    var y = time.getFullYear();
    var m = time.getMonth()+1;
    var d = time.getDate();
    var h = time.getHours();
    var mm = time.getMinutes();
    var s = time.getSeconds();
    return y+'-'+m+'-'+d+' '+addzero(h)+':'+addzero(mm)+':'+addzero(s);
  }

  //向服务器post
  $("#sm").bind("click", function () {
    if ($("#wish").val()) {
        $("#sm").button('loading');
        if (!$("#reward").val())
        {
          var reward = "无";
        }
        else
        {
          var reward = $("#reward").val();
        }
        if (!$("#contact").val())
        {
          var contact = "无";
        }
        else
        {
          var contact = $("#contact").val();
        }
        $.post("/makewish", {wish:$("#wish").val(),reward:reward,contact:contact,time:getFormatTime()},
            function (data) {
              alert(data);
              if (data == '成功提交~') {
                window.location.href = "/pool";
              }
          });
      } else {
        alert("愿望不能为空哦..");
      }
      $("#sm").button('reset');
    })
