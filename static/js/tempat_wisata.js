$(document).ready(function () {
    get_tempat_wisata()
  });

  function get_tempat_wisata() {
        $.ajax({
            type: "GET",
            url: "/tempat_wisata/get-tempat-wisata/"
        }).done((data) => {
            showWisata(data);
        });
    }

  function showWisata(kuliner) {
        const displayTable = $('.wrapper');
        displayTable.empty();
        kuliner.forEach(data => {
            const wisatacard = `
            <div class="card" style="width: 18rem; margin-right: auto; margin-left: auto; padding-bottom: 20; margin-top: 20px;">
            <div class="card-body">
            <h4 class="card-font">${data.fields.nama_tempat_wisata}</h4>
            <h6 class="card-text">${data.fields.provinsi_tempat_wisata}</h6>
            <p class="card-font">${data.fields.deskripsi_tempat_wisata}</p>
            <input type="submit" value="Delete Tempat Wisata"  class="submit" onclick="delete_tempat_kuliner(${data.pk})" />
        </div>
      </div>`
      ;
            displayTable.append(wisatacard);
        })
    };

    function add_tempat_wisata() {
      const form = $('.wisata-form');
      $.ajax({
        type: "POST",
        url: '/tempat_wisata/add-tempat-wisata/',
        data: form.serialize(), csrfmiddlewaretoken: '{{ csrf_token }}',
        error: console.log('error'),
        success: console.log('bisa'),
      }).done(function (data) {
        form.trigger('reset');
        get_tempat_wisata();
      });
      $("#staticBackdrop").modal("hide");
    }

    function delete_tempat_kuliner(id) {
        $.ajax({
            type: "GET",
            url: "/tempat_wisata/delete-tempat-wisata/" + id,
            data: {csrfmiddlewaretoken: '{{ csrf_token }}'}
        }).done((data) => {
            get_tempat_wisata();
        })
    }
    $(document).ready(function () {
      $('.navbar-light .dmenu').hover(function () {
              $(this).find('.sm-menu').first().stop(true, true).slideDown(150);
          }, function () {
              $(this).find('.sm-menu').first().stop(true, true).slideUp(105)
          });
      });
