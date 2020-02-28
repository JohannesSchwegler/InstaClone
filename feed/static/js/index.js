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
    $("#myModal").modal("show");

    $.ajax({
      type: "GET",
      url: "/get-followers/",
      contentType: "application/json",
      data: { userId: userId },
      success: response => {
        console.log(response.list);
        var body = $("#myModal").find(".modal-body");
        body.html("");
        response.list.forEach(item => {
          let container = $(`<div class="modal__user"></div`);
          let user = $(`<a href="/user/${item.username}">${item.username}</a>`);
          let image = $(`<img src="${item.userimage}" alt=""/>`);
          let follow = $(
            `<button class="btn btn-primary" data-user-id="${item.userId}">Follow</button>`
          );
          container.append(image, user, follow);
          body.append(container);
        });
      }
    });
  });

  $(".up a").on("click", function(e) {
    //var userId = $(this);
    e.preventDefault();

    let body = $("#myModal").find(".modal-body");
    let url = $(this).attr("href");

    console.log(body);

    body.load(url + " #post");
    window.history.pushState("page2", "Title", url);
    let data = $("#myModal").modal("show");
    /*
   $.ajax({
     type: "GET",
     url: "/get-followers/",
     contentType: "application/json",
     data: { userId: userId },
     success: response => {
       console.log(response.list);
       var body = $("#myModal").find(".modal-body");
       body.html("");
       response.list.forEach(item => {
         let container = $(`<div class="modal__user"></div`);
         let user = $(`<p>${item.username}</p>`);
         let image = $(`<img src="${item.userimage}" alt=""/>`);
         let follow = $(
           `<button class="btn btn-primary" data-user-id="${item.userId}">Follow</button>`
         );
         container.append(image, user, follow);
         body.append(container);
       });
     }
   });*/
  });
  handleSearch();
});

function handleSearch() {
  let input = $(".search");
  let searchBar = $(".search__container");
  let isOpen = false;
  input.on("input", function() {
    let container = $(".search__container").html("");
    let inputVal = input.val();
    if (inputVal === "") {
      return;
    }

    $.ajax({
      type: "GET",
      url: "/search/",
      contentType: "application/json",
      data: { inputVal },
      success: response => {
        response.list.forEach(item => {
          let itemContainer = $(
            `<a href="/user/${item.username}" class="search__item"></a>`
          );
          let innerContainer = $(`<div class="search__inner"></div>`);
          let user = $(`<p>${item.username}</p>`);
          let image = $(`<img src="${item.userimage}" alt=""/>`);

          container.append(
            itemContainer.append(innerContainer.append(image, user))
          );
          searchBar.css("display", "block");
          isOpen = true;

          console.log(item);
        });
      }
    });
  });

  input.on("click", function() {
    console.log("test");
    searchBar.css("display", "block");
    isOpen = true;
  });

  $(".container.my-5").on("click", function() {
    console.log("container");
    if (isOpen) {
      searchBar.css("display", "none");
    }
  });
}
