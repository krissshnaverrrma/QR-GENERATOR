document.addEventListener("DOMContentLoaded", () => {
 const form = document.getElementById('qrForm');
 const btn = document.querySelector('.btn-forge');
 if (form && btn) {
  form.onsubmit = () => {
   btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>Forging...';
   btn.classList.add('disabled');
   btn.style.pointerEvents = 'none';
  };
 }
});