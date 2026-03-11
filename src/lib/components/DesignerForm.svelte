<script lang="ts">
	import { toastState } from '$lib/state/toast.svelte';
	let { onSuccess } = $props();

	let name = $state('');
	let phone = $state('');
	let details = $state('');
	let isSubmitting = $state(false);
	let phoneError = $state('');

	function handlePhoneInput(e: Event) {
		const target = e.target as HTMLInputElement;

		// 1. Убираем всё, кроме цифр
		let value = target.value.replace(/\D/g, '');

		// 2. Ограничиваем длину (11 цифр для России: 7/8 + 10 цифр)
		if (value.length > 11) {
			value = value.slice(0, 11);
		}

		if (value.length === 0) {
			phone = '';
			phoneError = '';
			target.value = '';
			return;
		}

		// 3. Форматируем
		let formatted = '';
		let rawValue = value;

		if (rawValue.length > 0) {
			// Начинаем с +7 или +X (если первая цифра не 7 и не 8)
			if (rawValue[0] === '7' || rawValue[0] === '8') {
				formatted = '+7 ';
				rawValue = rawValue.slice(1);
			} else if (rawValue[0] === '9') {
				formatted = '+7 (9';
				rawValue = rawValue.slice(1);
			} else {
				formatted = '+' + rawValue[0] + ' ';
				rawValue = rawValue.slice(1);
			}
		}

		if (rawValue.length > 0) {
			if (value[0] !== '9') {
				formatted += '(' + rawValue.substring(0, 3);
			} else {
				formatted += rawValue.substring(0, 2);
			}
		}
		if (rawValue.length >= 3) {
			formatted += ') ' + rawValue.substring(3, 6);
		}
		if (rawValue.length >= 6) {
			formatted += '-' + rawValue.substring(6, 8);
		}
		if (rawValue.length >= 8) {
			formatted += '-' + rawValue.substring(8, 10);
		}

		phone = formatted;
		target.value = formatted;

		// Очищаем ошибку при вводе
		if (phoneError) phoneError = '';
	}

	function handlePhoneKeydown(e: KeyboardEvent) {
		const target = e.target as HTMLInputElement;
		const key = e.key;

		// Разрешаем: backspace, delete, стрелки, tab, ctrl/cmd+a, ctrl/cmd+c, ctrl/cmd+v, ctrl/cmd+x
		const isControlKey =
			key === 'Backspace' ||
			key === 'Delete' ||
			key === 'ArrowLeft' ||
			key === 'ArrowRight' ||
			key === 'ArrowUp' ||
			key === 'ArrowDown' ||
			key === 'Tab' ||
			e.ctrlKey ||
			e.metaKey;

		if (isControlKey) return;

		// Блокируем всё, что не является цифрой на уровне нажатия клавиши
		if (!/\d/.test(key)) {
			e.preventDefault();
			return;
		}

		// Блокируем ввод, если уже достигли максимальной длины 11 цифр (без учёта выделенного текста)
		const cleanPhone = target.value.replace(/\D/g, '');
		const hasSelection =
			target.selectionStart !== null && target.selectionStart !== target.selectionEnd;

		if (cleanPhone.length >= 11 && !hasSelection) {
			e.preventDefault();
		}
	}

	function handleSubmit(e: Event) {
		e.preventDefault();

		// Validate phone numbers: must contain 11 digits to submit (if started with 7/8/9)
		const cleanPhone = phone.replace(/\D/g, '');
		if (cleanPhone.length < 11) {
			phoneError = 'Некорректный номер телефона';
			return;
		} else {
			phoneError = '';
		}

		isSubmitting = true;

		// Simulate API call
		setTimeout(() => {
			isSubmitting = false;

			// Для демонстрации: С вероятностью 80% — успех, 20% — ошибка
			if (Math.random() > 0.2) {
				toastState.add({
					type: 'success',
					title: 'Заявка успешно отправлена',
					message: 'Наш дизайнер свяжется с вами в течение 15 минут.'
				});
				onSuccess?.();
			} else {
				toastState.add({
					type: 'error',
					title: 'Ошибка отправки',
					message: 'Не удалось отправить заявку. Пожалуйста, попробуйте позже или позвоните нам.',
					duration: 7000
				});
			}
		}, 1500);
	}
</script>

<form onsubmit={handleSubmit} class="flex flex-col gap-5">
	<div class="flex flex-col gap-2">
		<label class="text-xs tracking-wider text-text-secondary uppercase" for="name">Ваше имя</label>
		<input
			type="text"
			id="name"
			bind:value={name}
			class="border-b border-border-light bg-transparent py-3 text-primary transition-colors outline-none focus:border-secondary focus:ring-0"
			required
			placeholder="Иван Иванов"
		/>
	</div>

	<div class="relative flex flex-col gap-2">
		<label class="text-xs tracking-wider text-text-secondary uppercase" for="phone"
			>Номер телефона</label
		>
		<input
			type="tel"
			id="phone"
			value={phone}
			oninput={handlePhoneInput}
			onkeydown={handlePhoneKeydown}
			class="border-b border-border-light bg-transparent py-3 text-primary transition-colors outline-none focus:border-secondary focus:ring-0 {phoneError
				? 'border-red-500 focus:border-red-500'
				: ''}"
			required
			placeholder="+7 (___) ___-__-__"
		/>
		{#if phoneError}
			<span class="absolute -bottom-5 left-0 text-[10px] text-red-500">{phoneError}</span>
		{/if}
	</div>

	<div class="mt-2 flex flex-col gap-2">
		<label class="text-xs tracking-wider text-text-secondary uppercase" for="details"
			>Комментарий (опционально)</label
		>
		<textarea
			id="details"
			bind:value={details}
			rows={3}
			class="resize-none border-b border-border-light bg-transparent py-3 text-primary transition-colors outline-none focus:border-secondary focus:ring-0"
			placeholder="Удобное время для связи или адрес..."
		></textarea>
	</div>

	<button
		type="submit"
		disabled={isSubmitting}
		class="group mt-4 inline-flex items-center justify-center gap-3 border border-primary bg-primary px-8 py-4 text-xs tracking-[0.15em] text-text-inverse uppercase transition-all duration-500 hover:border-secondary hover:bg-secondary disabled:opacity-70"
	>
		{#if isSubmitting}
			<span
				class="inline-block h-4 w-4 animate-spin rounded-full border-2 border-white border-t-transparent"
			></span>
			Отправка...
		{:else}
			Вызвать дизайнера
			<svg
				class="h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
				fill="none"
				viewBox="0 0 24 24"
				stroke="currentColor"
				stroke-width="1.5"
			>
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
				/>
			</svg>
		{/if}
	</button>

	<p class="mt-2 text-center text-[10px] text-text-muted">
		Нажимая кнопку, вы соглашаетесь с политикой конфиденциальности.
	</p>
</form>
