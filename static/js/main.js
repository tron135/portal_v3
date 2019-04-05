// Hide Sections
$('.section').hide();

setTimeout(function () {
  $(document).ready(function () {
    // Show Sections
    $('.section').fadeIn();

    // Collapsible
    $('.collapsible').collapsible();

    // Hide Preloader
    $('.loader').fadeOut();

    //Init Side nav
    $('.sidenav').sidenav();

    // Init Modal
    $('.modal').modal();

    // Init Select
    $('select').formSelect();

    // Init Dropdown
    $('.dropdown-trigger').dropdown();

    // Quick ToDos
    $('#todo-form').submit(function (e) {
      const output = `<li class="collection-item">
          <div>${$('#todo').val()}
             <a href="#" class="secondary-content delete">
              <i class="material-icons">close</i>
            </a>
          </div>
        </li>`;
      $('.todos').append(output);

      Materialize.toast('ToDo Added', 3000)
      e.preventDefault();
    });

    // Delete Todos
    $('.todos').on('click', '.delete', function (e) {
      $(this).parent().parent().remove();
      Materialize.toast('ToDo Removed', 3000)
      e.preventDefault();
    });

  });
}, 1000);