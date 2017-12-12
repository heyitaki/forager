function openSidebar() {
  $("#sidebar-content-area").css("margin-right", '20px');
  $("#sidebar").width(275);
}

function closeSidebar() {
  $("#sidebar").width(0);
  $("#sidebar-content-area").css("margin-right", 0);
  $("#transparent-navbar i").removeClass("blue");
}

function quickSearch() {
  $("#search-bar").select();
}

function navigate(link) {
  window.location.href = `/${link}`;
}

$("#transparent-navbar i").click(function() {
  $(this).toggleClass("blue");
});

$(document).ready(function() {
  let altDown = false;
  $(document).keydown(function(e) {
    // Listen for alt/command press
    if (e.which == 18 || e.which == 91) {
      altDown = true;
    }

    // Quick search with alt+s
    if (altDown && e.which == 83) {
      quickSearch();
    }

    // Open sidebar with alt+i
    if (altDown && e.which == 73) {
      openSidebar();
    }

    // Close sidebar with esc/enter
    else if (e.which == 27 || e.which == 13) {
      closeSidebar();
    }
  });

  $(document).keyup(function(e) {
    // Listen for alt/command press end
    if (e.keyCode == 18 || e.keyCode == 91) {
      altDown = false;
    }
  });
});