function byteToMb(size) {
  return Math.round(Number(size) / 1024 / 1024 * 10) / 10
}

function createFileSet(id) {
  const upload_div = document.getElementById(id);
  upload_div.classList.add('upload_div');

  let init_msg = upload_div.innerHTML;
  if (!init_msg) {
    init_msg = '<div class="p-3"><i class="fas fa-cloud-upload-alt"></i> 마우스로 파일을 끌어오세요.</div>';
  }

  upload_div.innerHTML = `
    <div class="text-right">
      <label class="btn btn-primary">
        <input id="${ id }_button" type="file" multiple class="d-none">
        업로드
      </label>
    </div>
    <div id="${ id }_list">${ init_msg }</div>`;

  const file_set = new Proxy([], {
    set: function (target, prop, val) {
      target[prop] = val;
      if (prop === 'length') renderFiles(`${ id }_list`, file_set, init_msg)
      return true;
    }
  });

  initHandler(id, file_set);

  return file_set
}

function initHandler(id, proxy) {
  const upload_div = document.getElementById(id);
  const upload_btn = document.getElementById(`${ id }_button`)

  upload_div.ondragover = function (ev) {
    ev.preventDefault();
    document.getElementById(id).classList.add('drag_over')
  }

  upload_div.ondragleave = function (ev) {
    ev.preventDefault();
    document.getElementById(id).classList.remove('drag_over')
  }

  upload_div.ondrop = function (ev) {
    ev.preventDefault();
    document.getElementById(id).classList.remove('drag_over')

    if (ev.dataTransfer.items) {
      for (let i = 0; i < ev.dataTransfer.items.length; i++) {
        if (ev.dataTransfer.items[i].kind === 'file') {
          proxy.push(ev.dataTransfer.items[i].getAsFile());
        }
      }
    }
  }

  upload_btn.onchange = function (ev) {
    for (let i = 0; i < ev.target.files.length; i++) {
      proxy.push(ev.target.files[i]);
    }
  }
}

function renderFiles(id, proxy, msg) {
  if (proxy.length) {
    let count_file = 0;
    let sum_size = 0;

    msg = `
      <table class="upload_table">
        <tr>
          <th style="width: 70%">파일명</th>
          <th style="width: 20%">크기</th>
          <th style="width: 10%">삭제</th>
        </tr>`;

    for (let i = 0; i < proxy.length; i++) {
      msg += `
        <tr>
          <td>${ proxy[i].name }</td>
          <td class="text-right">${ byteToMb(proxy[i].size) } MB</td>
          <td id="${ id }_${ i }" class="cursor-pointer text-center"><i class="fa fa-times-circle"></td>
        </tr>`;

      count_file++;
      sum_size += proxy[i].size;
    }

    msg += `
      <tr>
        <th>${ count_file } 건</th>
        <th class="text-right">${ byteToMb(sum_size) } MB</th>
        <th></th>
      </tr>
      </table>`
    document.getElementById(id).innerHTML = msg;
    for (let i = 0; i < proxy.length; i++) {
      document.getElementById(`${id}_${i}`).onclick = function() {
        proxy.splice(i, 1);
      }
    }
  } else {
    document.getElementById(id).innerHTML = msg;
  }
}
