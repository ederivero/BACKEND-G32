const BASE_URL = 'http://localhost:5000'

let productoEditandoId = null



function setStatus(estado) {
  const dot = document.getElementById('statusDot')
  dot.className = 'header-dot ' + estado
}

let toastTimer = null
function showToast(mensaje, tipo) {
  const toast = document.getElementById('toast')
  toast.textContent = mensaje
  toast.className = 'show ' + tipo

  clearTimeout(toastTimer)
  toastTimer = setTimeout(function() {
    toast.className = ''
  }, 3000)
}

function mostrarMensajeTabla(icono, mensaje) {
  const tbody = document.getElementById('productosBody')
  tbody.innerHTML =
    '<tr>' +
      '<td colspan="5" class="table-empty">' +
        '<span>' + icono + '</span>' +
        mensaje +
      '</td>' +
    '</tr>'
  document.getElementById('countBadge').textContent = '0'
}



function switchTab(nombreTab) {
  const tabs = ['Crear', 'Editar', 'Buscar']

  tabs.forEach(function(tab) {
    const botonTab  = document.getElementById('tab'   + tab)
    const panelTab  = document.getElementById('panel' + tab)

    if (tab === nombreTab) {
      botonTab.classList.add('active')
      panelTab.classList.add('active')
    } else {
      botonTab.classList.remove('active')
      panelTab.classList.remove('active')
    }
  })
}



function cargarProductos() {
  const btn = document.getElementById('btnObtener')
  btn.disabled = true
  setStatus('loading')

  fetch(BASE_URL + '/productos')
    .then(function(respuesta) {
      return respuesta.json()
    })
    .then(function(datos) {
      setStatus('online')
      renderizarTabla(datos.content)
    })
    .catch(function(error) {
      setStatus('offline')
      mostrarMensajeTabla('🔴', 'No se pudo conectar con el servidor.')
      showToast('Error: ' + error.message, 'error')
    })
    .finally(function() {
      btn.disabled = false
    })
}

function renderizarTabla(productos) {
  const tbody = document.getElementById('productosBody')
  const badge = document.getElementById('countBadge')

  badge.textContent = productos.length

  if (productos.length === 0) {
    mostrarMensajeTabla('📋', 'No hay productos registrados.')
    return
  }

  tbody.innerHTML = ''

  productos.forEach(function(producto) {
    const precio = Number(producto.precio || 0).toFixed(2)

    const fila = document.createElement('tr')

    fila.innerHTML =
      '<td class="td-id">#' + producto.id + '</td>' +
      '<td class="td-nombre">' + producto.nombre + '</td>' +
      '<td class="td-precio">S/. ' + precio + '</td>' +
      '<td class="td-cantidad">' + producto.cantidad + '</td>' +
      '<td class="td-actions">' +
        '<button class="btn-icon btn-edit" ' +
          'onclick="prepararEdicion(' + producto.id + ', \'' + producto.nombre + '\', ' + (producto.precio || 0) + ', ' + producto.cantidad + ')">' +
          '✏️ Editar' +
        '</button> ' +
        '<button class="btn-icon btn-del" ' +
          'onclick="confirmarEliminar(' + producto.id + ', \'' + producto.nombre + '\')">' +
          '🗑 Eliminar' +
        '</button>' +
      '</td>'

    tbody.appendChild(fila)
  })
}



function crearProducto(evento) {
  evento.preventDefault()

  const btn = document.getElementById('btnCrear')

  const datos = {
    nombre:   document.getElementById('cNombre').value,
    precio:   parseFloat(document.getElementById('cPrecio').value),
    cantidad: parseInt(document.getElementById('cCantidad').value)
  }

  btn.disabled = true
  btn.innerHTML = '<div class="spinner"></div> Creando…'

  fetch(BASE_URL + '/productos', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'  
    },
    body: JSON.stringify(datos)           
  })
    .then(function(respuesta) {
      return respuesta.json()
    })
    .then(function(resultado) {
      showToast('✓ ' + resultado.message, 'success')
      document.getElementById('formCrear').reset()
      cargarProductos()   
    })
    .catch(function(error) {
      showToast('Error: ' + error.message, 'error')
    })
    .finally(function() {
      btn.disabled = false
      btn.innerHTML = 'Crear producto'
    })
}



function buscarProducto(evento) {
  evento.preventDefault()

  const id  = document.getElementById('bId').value
  const btn = document.getElementById('btnBuscar')
  const resultado = document.getElementById('resultadoBuscar')

  resultado.hidden = true

  btn.disabled = true
  btn.innerHTML = '<div class="spinner"></div> Buscando…'

  fetch(BASE_URL + '/producto/' + id)
    .then(function(respuesta) {
      return respuesta.json()
    })
    .then(function(datos) {
      const producto = datos.content

      if (!producto) {
        showToast('Producto no encontrado', 'error')
        return
      }

      document.getElementById('rId').value       = producto.id
      document.getElementById('rNombre').value   = producto.nombre
      document.getElementById('rPrecio').value   = 'S/. ' + Number(producto.precio || 0).toFixed(2)
      document.getElementById('rCantidad').value = producto.cantidad

      resultado.hidden = false
    })
    .catch(function(error) {
      showToast('Error: ' + error.message, 'error')
    })
    .finally(function() {
      btn.disabled = false
      btn.innerHTML = 'Buscar'
    })
}



function prepararEdicion(id, nombre, precio, cantidad) {
  productoEditandoId = id

  document.getElementById('editHint').textContent = 'Editando producto #' + id

  document.getElementById('eNombre').value   = nombre
  document.getElementById('ePrecio').value   = precio
  document.getElementById('eCantidad').value = cantidad

  document.getElementById('btnActualizar').disabled = false
  document.getElementById('btnEliminar').disabled   = false

  switchTab('Editar')
}

function actualizarProducto(evento) {
  evento.preventDefault()

  if (!productoEditandoId) return

  const btn = document.getElementById('btnActualizar')

  const datos = {
    nombre:   document.getElementById('eNombre').value,
    precio:   parseFloat(document.getElementById('ePrecio').value),
    cantidad: parseInt(document.getElementById('eCantidad').value)
  }

  btn.disabled = true
  btn.innerHTML = '<div class="spinner"></div> Actualizando…'

  fetch(BASE_URL + '/producto/' + productoEditandoId, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(datos)
  })
    .then(function(respuesta) {
      return respuesta.json()
    })
    .then(function(resultado) {
      showToast('✓ ' + resultado.message, 'success')
      limpiarFormEditar()
      cargarProductos()
      switchTab('Crear')
    })
    .catch(function(error) {
      showToast('Error: ' + error.message, 'error')
    })
    .finally(function() {
      btn.disabled = false
      btn.innerHTML = 'Actualizar'
    })
}



function confirmarEliminar(id, nombre) {
  prepararEdicion(id, nombre, 0, 0)
}

function eliminarProducto() {
  if (!productoEditandoId) return

  const btn = document.getElementById('btnEliminar')

  btn.disabled = true
  btn.innerHTML = '<div class="spinner"></div>'

  fetch(BASE_URL + '/producto/' + productoEditandoId, {
    method: 'DELETE'
  })
    .then(function(respuesta) {
      return respuesta.json()
    })
    .then(function(resultado) {
      showToast('✓ ' + (resultado.message || 'Producto eliminado'), 'success')
      limpiarFormEditar()
      cargarProductos()
      switchTab('Crear')
    })
    .catch(function(error) {
      showToast('Error: ' + error.message, 'error')
    })
    .finally(function() {
      btn.disabled = false
      btn.innerHTML = 'Eliminar'
    })
}

function limpiarFormEditar() {
  productoEditandoId = null
  document.getElementById('formEditar').reset()
  document.getElementById('editHint').textContent = 'Haz clic en ✏️ de la tabla para editar un producto.'
  document.getElementById('btnActualizar').disabled = true
  document.getElementById('btnEliminar').disabled   = true
}



document.getElementById('btnObtener').addEventListener('click', cargarProductos)
document.getElementById('formCrear').addEventListener('submit', crearProducto)
document.getElementById('formEditar').addEventListener('submit', actualizarProducto)
document.getElementById('formBuscar').addEventListener('submit', buscarProducto)
document.getElementById('btnEliminar').addEventListener('click', eliminarProducto)

document.getElementById('tabCrear').addEventListener('click', function() { switchTab('Crear') })
document.getElementById('tabEditar').addEventListener('click', function() { switchTab('Editar') })
document.getElementById('tabBuscar').addEventListener('click', function() { switchTab('Buscar') })



cargarProductos()
