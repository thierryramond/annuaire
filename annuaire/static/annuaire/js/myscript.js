// En français, et mise en page (dom)

 var table = $('#tri').DataTable({
      //ajax: '/api/staff',
      //dom:  'Tfrtip', 
      //tableTools: {
      //  sRowSelect: 'os',
      //},
      "dom": '<"top" lf>t<"bottom" ip><"clear">',
      "autowidth": true,
       paging: false,
       "lengthMenu": [ [30, 50, 100,-1], [30, 50, 100,"tous les"] ],
       "language":{
          "sSearch":  "Rechercher&nbsp;: ",
          "sLengthMenu": "Afficher _MENU_ &eacute;l&eacute;ments",
          "sInfo":   "Affichage des &eacute;l&eacute;ments _START_ &agrave; _END_ sur _TOTAL_ &eacute;l&eacute;ments",
          "oPaginate": {
            "sFirst":      "Premier",
            "sPrevious":   "Pr&eacute;c&eacute;dent",
            "sNext":       "Suivant",
            "sLast":       "Dernier"
          },
          "sInfoFiltered":   "(filtr&eacute; de _MAX_ &eacute;l&eacute;ments au total)",
          "sZeroRecords":    "Aucun &eacute;l&eacute;ment &agrave; afficher",
          "sEmptyTable":     "Aucune donn&eacute;e disponible dans le tableau",
          "sInfoEmpty":      "Affichage de l'&eacute;l&eacute;ment 0 &agrave; 0 sur 0 &eacute;l&eacute;ments",
        }
    });


// Prendre en compte les filtres

$('#tri tfoot th').each( function () {
        var title = $('#tri thead th').eq( $(this).index() ).text();
        $(this).html( '<input type="text" placeholder="filtrer" />' );
    });


// Apply the search
table.columns().every( function () {
      var that = this;

      $( 'input', this.footer() ).on( 'keyup change', function () {
          that
              .search( this.value )
              .draw();
      });
    });
