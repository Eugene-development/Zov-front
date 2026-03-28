<script lang="ts">
	import { toastState } from '$lib/state/toast.svelte';
	import { getAuthApiUrl } from '$lib/utils/config.js';
	import { onMount } from 'svelte';

	let { onSuccess } = $props();

	let name = $state('');
	let phone = $state('');
	let isSubmitting = $state(false);
	let phoneError = $state('');
	let promoCode = $state('');
	let submitted = $state(false);

	// Generate promo code based on UTM ad id or fallback to 'seo'
	function generatePromoCode(): string {
		if (typeof window === 'undefined') return 'ZOV-SEO-10';

		const params = new URLSearchParams(window.location.search);
		// Check utm_content, utm_term, or a custom ad param for the ad id
		const adId =
			params.get('utm_content') ||
			params.get('utm_term') ||
			params.get('ad_id') ||
			params.get('yclid') ||
			null;

		if (adId) {
			// Sanitize and truncate to keep it clean
			const sanitized = adId
				.replace(/[^a-zA-Z0-9]/g, '')
				.toUpperCase()
				.slice(0, 8);
			return `ZOV-${sanitized}-10`;
		}
		return 'ZOV-SEO-10';
	}

	function handlePhoneInput(e: Event) {
		const target = e.target as HTMLInputElement;
		let value = target.value.replace(/\D/g, '');
		if (value.length > 11) value = value.slice(0, 11);

		if (value.length === 0) {
			phone = '';
			phoneError = '';
			target.value = '';
			return;
		}

		let formatted = '';
		let rawValue = value;

		if (rawValue.length > 0) {
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
		if (rawValue.length >= 3) formatted += ') ' + rawValue.substring(3, 6);
		if (rawValue.length >= 6) formatted += '-' + rawValue.substring(6, 8);
		if (rawValue.length >= 8) formatted += '-' + rawValue.substring(8, 10);

		phone = formatted;
		target.value = formatted;
		if (phoneError) phoneError = '';
	}

	function handlePhoneKeydown(e: KeyboardEvent) {
		const target = e.target as HTMLInputElement;
		const key = e.key;
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
		if (!/\d/.test(key)) {
			e.preventDefault();
			return;
		}

		const cleanPhone = target.value.replace(/\D/g, '');
		const hasSelection =
			target.selectionStart !== null && target.selectionStart !== target.selectionEnd;
		if (cleanPhone.length >= 11 && !hasSelection) e.preventDefault();
	}

	async function handleSubmit(e: Event) {
		e.preventDefault();

		const cleanPhone = phone.replace(/\D/g, '');
		if (cleanPhone.length < 11) {
			phoneError = 'Некорректный номер телефона';
			return;
		} else {
			phoneError = '';
		}

		isSubmitting = true;
		const code = generatePromoCode();

		try {
			const sourceUrl = typeof window !== 'undefined' ? window.location.href : '';

			const requestData = {
				form_type: 'promo-code',
				name: name.trim(),
				phone: phone,
				message: `Промокод: ${code}`,
				source_url: sourceUrl
			};

			const authApiUrl = getAuthApiUrl();
			const response = await fetch(`${authApiUrl}/notify/service-request`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
					Accept: 'application/json'
				},
				body: JSON.stringify(requestData)
			});

			const result = await response.json();

			if (!response.ok || !result.success) {
				throw new Error(result.message || 'Ошибка отправки');
			}

			promoCode = code;
			submitted = true;

			toastState.add({
				type: 'success',
				title: 'Промокод сформирован',
				message: 'С вами в ближайшее время свяжется наш менеджер и передаст промокод.'
			});

			if (typeof window !== 'undefined' && (window as any).ym) {
				(window as any).ym(93835019, 'reachGoal', 'promo_code_target');
			}
		} catch (err) {
			console.error('PromoCodeForm submit error:', err);
			toastState.add({
				type: 'error',
				title: 'Ошибка отправки',
				message: 'Не удалось отправить заявку. Пожалуйста, попробуйте позже или позвоните нам.',
				duration: 7000
			});
		} finally {
			isSubmitting = false;
		}
	}
</script>

{#if submitted}
	<!-- Success State -->
	<div class="flex flex-col items-center gap-6 py-4 text-center">
		<div
			class="flex h-16 w-16 items-center justify-center rounded-full border border-accent/30 bg-accent/10"
		>
			<svg class="h-8 w-8 text-accent" fill="none" viewBox="0 0 24 24" stroke="currentColor">
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="1.5"
					d="M4.5 12.75l6 6 9-13.5"
				/>
			</svg>
		</div>

		<div>
			<p class="text-sm text-secondary">Ваш уникальный промокод на скидку 10%</p>
			<div
				class="mt-4 flex items-center justify-center gap-3 border border-dashed border-secondary/40 bg-surface-warm px-6 py-4"
			>
				<span class="font-mono text-2xl font-semibold tracking-widest text-primary"
					>{promoCode}</span
				>
			</div>
			<p class="mt-4 text-xs text-muted">
				Сохраните этот промокод и назовите его менеджеру при заказе — вы получите скидку 10% на свою
				кухню или шкаф.
			</p>
		</div>

		<button
			onclick={() => onSuccess?.()}
			class="mt-2 inline-flex items-center gap-2 rounded-sm border border-primary bg-primary px-8 py-3 text-xs tracking-[0.15em] text-inverse uppercase transition-all duration-500 hover:border-secondary hover:bg-secondary"
		>
			Отлично, спасибо!
		</button>
	</div>
{:else}
	<!-- Info block -->
	<div class="mb-6 border-l-2 border-accent pl-4">
		<p class="text-sm leading-relaxed text-secondary">
			Заполните форму ниже, и мы сформируем уникальный промокод на
			<strong class="text-primary">скидку 10%</strong> на любую кухню или шкаф-купе от фабрики ЗОВ.
		</p>
		<p class="mt-2 text-xs text-muted">
			Промокод действует при заказе в любом фирменном салоне ЗОВ.
		</p>
	</div>

	<form onsubmit={handleSubmit} class="flex flex-col gap-5">
		<div class="flex flex-col gap-2">
			<label class="text-xs tracking-wider text-secondary uppercase" for="promo-name"
				>Ваше имя</label
			>
			<input
				type="text"
				id="promo-name"
				bind:value={name}
				class="border-b border-border-light bg-transparent py-3 text-primary transition-colors outline-none focus:border-secondary focus:ring-0"
				required
				placeholder="Иван Иванов"
			/>
		</div>

		<div class="relative flex flex-col gap-2">
			<label class="text-xs tracking-wider text-secondary uppercase" for="promo-phone"
				>Номер телефона</label
			>
			<input
				type="tel"
				id="promo-phone"
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

		<button
			type="submit"
			disabled={isSubmitting}
			class="group mt-6 inline-flex items-center justify-center gap-3 rounded-sm border border-primary bg-primary px-8 py-4 text-xs tracking-[0.15em] text-inverse uppercase transition-all duration-500 hover:border-secondary hover:bg-secondary disabled:opacity-70"
		>
			{#if isSubmitting}
				<span
					class="inline-block h-4 w-4 animate-spin rounded-full border-2 border-white border-t-transparent"
				></span>
				Отправка...
			{:else}
				Получить промокод
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

		<p class="mt-2 text-center text-[10px] text-muted">
			Нажимая кнопку, вы соглашаетесь с политикой конфиденциальности.
		</p>
	</form>
{/if}
