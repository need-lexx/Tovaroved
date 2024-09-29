var x = 0;

function addInput() {
	if (x < 10) {
    var str = '<p><select name="title" class="link" required id="id_title" *"></p> <p><input type="number" name="count" class="amount" placeholder="Кол-во" required id="id_count"><p/> <div id="input' + (x + 1) + '"></div>';
    document.getElementById('input' + x).innerHTML = str;
    x++;
  } else
  {
  	alert('STOP it!');
  }
}