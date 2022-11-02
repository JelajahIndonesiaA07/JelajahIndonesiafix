$(document).ready(function () {
    get_tempat_kuliner()
  });

  function get_tempat_kuliner() {
        $.ajax({
            type: "GET",
            url: "/tempat_kuliner/get-tempat-kuliner/"
        }).done((data) => {
            showKuliner(data);
        });
    }

  function showKuliner(kuliner) {
        const displayTable = $('.wrapper');
        displayTable.empty();
        kuliner.forEach(data => {
            const kulinerCard = `
            <div class="card" style="width: 18rem; margin-right: auto; margin-left: auto; padding-bottom: 20; margin-top: 20px;">
            <div class="card-body">
            <h4 class="card-font">${data.fields.nama_tempat_kuliner}</h4>
            <h6 class="card-text">${data.fields.rating_tempat_kuliner}</h6>
            <p class="card-font">${data.fields.lokasi_tempat_kuliner}</p>
            <input type="submit" value="Delete Tempat Kuliner"  class="submit" onclick="delete_tempat_kuliner(${data.pk})" />
        </div>
      </div>`
      ;
            displayTable.append(kulinerCard);
        })
    };

    function add_tempat_kuliner() {
      const form = $('.kuliner-form');
      $.ajax({
        type: "POST",
        url: '/tempat_kuliner/add-tempat-kuliner/',
        data: form.serialize(), csrfmiddlewaretoken: '{{ csrf_token }}',
      }).done(function (data) {
        form.trigger('reset');
        get_tempat_kuliner();
      });
      $("#staticBackdrop").modal("hide");
    }

    function delete_tempat_kuliner(id) {
        $.ajax({
            type: "GET",
            url: "/tempat_kuliner/delete-tempat-kuliner/" + id,
            data: {csrfmiddlewaretoken: '{{ csrf_token }}'}
        }).done((data) => {
            get_tempat_kuliner();
        })
    }
    $(document).ready(function () {
      $('.navbar-light .dmenu').hover(function () {
              $(this).find('.sm-menu').first().stop(true, true).slideDown(150);
          }, function () {
              $(this).find('.sm-menu').first().stop(true, true).slideUp(105)
          });
      });
