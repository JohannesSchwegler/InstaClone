window.addEventListener("load", () => {
  let sidebar = document.querySelector(".sidebar");

  //sidebar.style.left=window.innerWidth-495+"px";

  window.addEventListener("resize", () => {
    // let width= window.innerWidth;
  });

  // this is the id of the form
  $(".submitComment").submit(function(e) {
    e.preventDefault(); // avoid to execute the actual submit of the form.

    var form = $(this);
    var url = form.attr("action");
    var comment = $(this)
      .find("textarea")
      .val();
    var postId = $(this)
      .find("button")
      .data().postId;

    $.ajax({
      type: "POST",
      url: "/add-comment/",
      data: JSON.stringify({ comment, postId }),
      success: function(data) {
        $(".post__comments").append(
          `<p><span>${data.user}:</span><span>${data.comment}</span></p>`
        );
      }
    });
  });

  /*
   $.ajax({
     type: "POST",
     url: "yourURL", // where you wanna post
     data: formData,
     processData: false,
     contentType: false,
     error: function(jqXHR, textStatus, errorMessage) {
       console.log(errorMessage); // Optional
     },
     success: function(data) {
       console.log(data);
     }
   });*/

  $(".post__like").on("click", function() {
    postId = $(this).data().postId;

    $.ajax({
      type: "POST",
      url: "/add-like/",
      data: JSON.stringify({ postId }),
      success: message => {
        if (message.like === "remove") {
          removeAddLike($(this), -1);
        } else {
          removeAddLike($(this), 1);
        }
      }
    });
  });

  function removeAddLike(element, value) {
    element.find("svg").toggleClass("liked");

    let current = element
      .parent()
      .parent()
      .find(".post__likes span")
      .text();
    console.log(parseInt(current) + value);

    $(".post__likes span").html(parseInt(current) + value);
  }

  $(".profile__follow").on("click", function() {
    userId = $(this).data().userId;
    $.ajax({
      type: "POST",
      url: "/add-follower/",
      data: JSON.stringify({ userId }),
      success: message => {
        console.log("erfolgreich");
      }
    });
  });

  $(".profile__follower").on("click", function() {
    var userId = $(this).data().userId;
    console.log(userId);
    $.ajax({
      type: "GET",
      url: "/get-followers/",
      contentType: "application/json",
      data: { userId: userId },
      success: response => {
        console.log(response.list[0]);
      }
    });
  });
});
