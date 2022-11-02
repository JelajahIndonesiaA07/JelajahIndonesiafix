$(document).ready(function () {
    getHospital()
  });

  function getHospital() {
        $.ajax({
            type: "GET",
            url: "/emergencycall/get-hospital/"
        }).done((data) => {
            console.log('showing')
            showHospital(data);
        });
    }
    

  function showHospital(hospitals) {
        const displayTable = $('.wrapper');
        displayTable.empty();
        hospitals.forEach(data => {
            const hospitalCard = `
            <div class="card" style="width: 18rem; margin-right: auto; margin-left: auto; padding-bottom: 20; margin-top: 20px;">
                <div class="card-body">
                    <h4 class="card-font">${data.fields.hospital_name}</h4>
                    <h6 class="card-text">0${data.fields.hospital_number}</h6>
                    <p class="card-font">${data.fields.hospital_location}</p>
                    <input type="submit" value="Delete Hospital"  class="submit" onclick="delete_hospital(${data.pk})" />
                </div>
            </div>`;
            displayTable.append(hospitalCard);
        })
    };

    function newHospital() {
      const form = $('.hospital-form');
      $.ajax({
        type: "POST",
        url: '/emergencycall/new-hospital/',
        data: form.serialize(), 
        csrfmiddlewaretoken: '{{ csrf_token }}',
        error: console.log('error'),
        success: console.log('bisa'),
      }).done(function (data) {
        form.trigger('reset');
        console.log('getHospital?');
        getHospital();
      });
      $("#staticBackdrop").modal("hide");
    }

    function delete_hospital(id) {
        $.ajax({
            type: "GET",
            url: "/emergencycall/hapus/" + id,
            data: {csrfmiddlewaretoken: '{{ csrf_token }}'}
        }).done((data) => {
            getHospital();
        })
    }
