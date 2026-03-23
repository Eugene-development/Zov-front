<script lang="ts">
	import { toastState } from '$lib/state/toast.svelte';
	import { getAuthApiUrl } from '$lib/utils/config.js';
	let { onSuccess } = $props();

	let step = $state(0);
	let answers = $state({
		layout: '',
		style: '',
		timeframe: ''
	});
	let name = $state('');
	let phone = $state('');
	let isSubmitting = $state(false);
	let phoneError = $state('');

	const questions = [
		{
			id: 'layout',
			title: 'Какая планировка кухни вам нравится?',
			options: ['Прямая', 'Угловая', 'П-образная', 'С островом']
		},
		{
			id: 'style',
			title: 'Какой стиль предпочитаете?',
			options: ['Современный', 'Классика', 'Лофт', 'Минимализм']
		},
		{
			id: 'timeframe',
			title: 'Когда планируете начать проект?',
			options: ['В этом месяце', 'Через 1-3 месяца', 'Полгода и более']
		}
	];

	function nextStep(option: string, questionId: string) {
		answers[questionId as keyof typeof answers] = option;
		step++;
	}

	function handlePhoneInput(e: Event) {
		const target = e.target as HTMLInputElement;
		let value = target.value.replace(/\D/g, '');

		if (value.length > 11) {
			value = value.slice(0, 11);
		}

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

		if (cleanPhone.length >= 11 && !hasSelection) {
			e.preventDefault();
		}
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

		try {
			const sourceUrl = typeof window !== 'undefined' ? window.location.href : '';

			const requestData = {
				form_type: 'quiz',
				name: name.trim(),
				phone: phone,
				source_url: sourceUrl,
				extra: {
					'Планировка кухни': answers.layout,
					'Предпочтительный стиль': answers.style,
					'Планируемые сроки': answers.timeframe
				}
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

			toastState.add({
				type: 'success',
				title: 'Тест успешно пройден',
				message: 'Наш дизайнер свяжется с вами для обсуждения цены и деталей проекта.'
			});
			onSuccess?.();
		} catch (err) {
			console.error('QuizForm submit error:', err);
			toastState.add({
				type: 'error',
				title: 'Ошибка отправки',
				message: 'Не удалось отправить заявку. Пожалуйста, попробуйте позже.',
				duration: 7000
			});
		} finally {
			isSubmitting = false;
		}
	}
</script>

<div class="flex flex-col gap-5">
	{#if step === 0}
		<div class="py-2 text-center">
			<p class="mx-auto mb-6 text-sm leading-relaxed text-secondary">
				Ответьте на несколько простых вопросов о вашей будущей кухне, и мы рассчитаем ее примерную
				стоимость
			</p>
			<p class="mx-auto mb-8 text-sm leading-relaxed text-secondary">
				А также подарим гарантированный бонус — промокод на скидку 10% на любую корпусную мебель,
				комплект сантехники, столешницу или бытовую технику
			</p>
			<button
				type="button"
				onclick={() => (step = 1)}
				class="group inline-flex w-full cursor-pointer items-center justify-center gap-3 rounded-sm bg-primary px-10 py-5 text-xs font-medium tracking-[0.2em] text-inverse uppercase shadow-xl shadow-primary/10 transition-all duration-500 hover:-translate-y-1 hover:bg-secondary hover:shadow-2xl hover:shadow-secondary/20"
			>
				Начать расчет
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
			</button>
		</div>
	{:else if step <= questions.length}
		<!-- Quiz step -->
		<div class="mb-4">
			<h3 class="mb-6 text-xl font-light text-primary" style="font-family: var(--font-heading);">
				Шаг {step} из {questions.length}
			</h3>
			<p class="mb-6 text-base text-secondary">{questions[step - 1].title}</p>

			<div class="flex flex-col gap-3">
				{#each questions[step - 1].options as option}
					<button
						class="w-full border border-border-light p-4 text-left text-sm transition-colors duration-300 hover:border-secondary"
						onclick={() => nextStep(option, questions[step - 1].id)}
					>
						{option}
					</button>
				{/each}
			</div>
		</div>
	{:else}
		<!-- Final step (Contact form) -->
		<div class="mb-4">
			<h3 class="mb-2 text-xl font-light text-primary" style="font-family: var(--font-heading);">
				Отлично! Информация получена.
			</h3>
			<p class="mb-6 text-sm text-secondary">
				Оставьте свои контакты, чтобы мы могли отправить вам итоги расчета и ваш бонусный промокод
				на скидку 10% на любую корпусную мебель, комплект сантехники, столешницу или бытовую
				технику.
			</p>

			<form onsubmit={handleSubmit} class="flex flex-col gap-5">
				<div class="flex flex-col gap-2">
					<label class="text-xs tracking-wider text-secondary uppercase" for="name">Ваше имя</label>
					<input
						type="text"
						id="name"
						bind:value={name}
						class="border-b border-border-light bg-transparent py-3 text-primary transition-colors outline-none focus:border-secondary focus:ring-0"
						required
						placeholder=""
					/>
				</div>

				<div class="relative flex flex-col gap-2">
					<label class="text-xs tracking-wider text-secondary uppercase" for="phone"
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
						Получить расчет и промокод
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
		</div>
	{/if}
</div>
