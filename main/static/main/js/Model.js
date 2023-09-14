//модальное окно для услуги массаж

$(function () {
  $('#services_massage').click(function () {
    $('#modal-1').addClass('modal_active');
    $('html').addClass('hidden');
  });
 
  $('.modal__close-button').click(function () {
    $('#modal-1').removeClass('modal_active');
    $('html').removeClass('hidden');
  });
 
  $('#modal-1').mouseup(function (e) {
    let modalContent = $(".modal__content");
    if (!modalContent.is(e.target) && modalContent.has(e.target).length === 0) {
      $(this).removeClass('modal_active');
      $('html').removeClass('hidden');
    }
  });
});

//модальное окно для услуги спа-программа
$(function () {
  $('#services_spa_program').click(function () {
    $('#modal-2').addClass('modal_active');
    $('html').addClass('hidden');
  });

  $('.modal__close-button').click(function () {
    $('#modal-2').removeClass('modal_active');
    $('html').removeClass('hidden');
  });

  $('#modal-2').mouseup(function (e) {
    let modalContent = $(".modal__content");
    if (!modalContent.is(e.target) && modalContent.has(e.target).length === 0) {
      $(this).removeClass('modal_active');
      $('html').removeClass('hidden');
    }
  });
});


//модальное окно для услуги тейпирование
$(function () {
  $('#services_taping').click(function () {
    $('#modal-3').addClass('modal_active');
    $('html').addClass('hidden');
  });

  $('.modal__close-button').click(function () {
    $('#modal-3').removeClass('modal_active');
    $('html').removeClass('hidden');
  });

  $('#modal-3').mouseup(function (e) {
    let modalContent = $(".modal__content");
    if (!modalContent.is(e.target) && modalContent.has(e.target).length === 0) {
      $(this).removeClass('modal_active');
      $('html').removeClass('hidden');
    }
  });
});


//модальное окно для услуги обучения
$(function () {
  $('#services_obuchine').click(function () {
    $('#modal-4').addClass('modal_active');
    $('html').addClass('hidden');
  });

  $('.modal__close-button').click(function () {
    $('#modal-4').removeClass('modal_active');
    $('html').removeClass('hidden');
  });

  $('#modal-4').mouseup(function (e) {
    let modalContent = $(".modal__content");
    if (!modalContent.is(e.target) && modalContent.has(e.target).length === 0) {
      $(this).removeClass('modal_active');
      $('html').removeClass('hidden');
    }
  });
});



//модальное окно для формы обратной связи массаж
$(function () {
  $('#application_b').click(function () {
    $('#modal-5').addClass('modal_active');
    $('html').addClass('hidden');
  });

  $('.modal__close-button').click(function () {
    $('#modal-5').removeClass('modal_active');
    $('html').removeClass('hidden');
  });

  $('#modal-5').mouseup(function (e) {
    let modalContent = $(".modal__content");
    if (!modalContent.is(e.target) && modalContent.has(e.target).length === 0) {
      $(this).removeClass('modal_active');
      $('html').removeClass('hidden');
    }
  });
});