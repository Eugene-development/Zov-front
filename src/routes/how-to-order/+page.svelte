<script>
	import { onMount } from 'svelte';
	import Modal from '$lib/components/Modal.svelte';
	import DesignerForm from '$lib/components/DesignerForm.svelte';
	import ConsultationForm from '$lib/components/ConsultationForm.svelte';

	let heroVisible = $state(false);
	let isDesignerModalOpen = $state(false);
	let isConsultationModalOpen = $state(false);
	let sections = $state({});

	onMount(() => {
		heroVisible = true;

		const observer = new IntersectionObserver(
			(entries) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting) {
						sections[entry.target.id] = true;
					}
				});
			},
			{ threshold: 0.1, rootMargin: '0px 0px -50px 0px' }
		);

		document.querySelectorAll('[data-animate]').forEach((el) => {
			observer.observe(el);
		});

		return () => observer.disconnect();
	});

	const steps = [
		{
			title: 'Консультация',
			description:
				'Свяжитесь с нами любым удобным способом. Мы ответим на ваши вопросы, сориентируем по стилям и материалам, подберем оптимальное решение для вашего интерьера.',
			icon: 'M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.373 5.486-1.071 1.637-2.67 3.036-2.67 3.036s1.657-.59 3.518-1.077A9.098 9.098 0 0012 20.25z'
		},
		{
			title: 'Выезд в салон партнёра',
			description:
				'Приглашаем вас посетить один из наших салонов, чтобы лично оценить качество фасадов, фурнитуры и готовых решений, а также обсудить детали с дизайнером.',
			icon: 'M13.5 21v-7.5a.75.75 0 01.75-.75h3a.75.75 0 01.75.75V21m-4.5 0H2.36m11.14 0H18m0 0h3.64m-1.39 0V9.349m-16.5 11.65V9.35m0 0a3.001 3.001 0 003.75-.615A2.999 2.999 0 009.75 9.75c.896 0 1.7-.393 2.25-1.016a2.999 2.999 0 002.25 1.016c.896 0 1.7-.393 2.25-1.015a3.001 3.001 0 003.75.614m-16.5 0a3.004 3.004 0 01-.621-4.72L4.318 3.44A1.5 1.5 0 015.378 3h13.243a1.5 1.5 0 011.06.44l1.19 1.189a3 3 0 01-.621 4.72m-13.5 8.65h3.75a.75.75 0 00.75-.75V13.5a.75.75 0 00-.75-.75H6.75a.75.75 0 00-.75.75v3.75c0 .415.336.75.75.75z'
		},
		{
			title: 'Проектный замер',
			description:
				'Наш квалифицированный специалист приедет к вам для точного замера помещения, учитывая все архитектурные особенности, ниши и расположение коммуникаций.',
			icon: 'M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0 4.5L15 15'
		},
		{
			title: 'Составление дизайн проекта',
			description:
				'Опираясь на ваши пожелания и данные замера, профессиональный дизайнер разработает фотореалистичную 3D-модель вашей будущей стильной мебели с идеальной эргономикой.',
			icon: 'M3.75 6A2.25 2.25 0 016 3.75h2.25A2.25 2.25 0 0110.5 6v2.25a2.25 2.25 0 01-2.25 2.25H6a2.25 2.25 0 01-2.25-2.25V6zM3.75 15.75A2.25 2.25 0 016 13.5h2.25a2.25 2.25 0 012.25 2.25V18a2.25 2.25 0 01-2.25 2.25H6A2.25 2.25 0 013.75 18v-2.25zM13.5 6a2.25 2.25 0 012.25-2.25H18A2.25 2.25 0 0120.25 6v2.25A2.25 2.25 0 0118 10.5h-2.25a2.25 2.25 0 01-2.25-2.25V6zM13.5 15.75a2.25 2.25 0 012.25-2.25H18a2.25 2.25 0 012.25 2.25V18A2.25 2.25 0 0118 20.25h-2.25A2.25 2.25 0 0113.5 18v-2.25z'
		},
		{
			title: 'Просчёт проекта',
			description:
				'Мы подготовим для вас прозрачную и подробную смету с учётом выбранных материалов, фурнитуры, внутреннего наполнения и дополнительных элементов.',
			icon: 'M15.75 15.75V18m-7.5-6.75h.008v.008H8.25v-.008zm0 2.25h.008v.008H8.25V13.5zm0 2.25h.008v.008H8.25v-.008zm0 2.25h.008v.008H8.25V18zm2.498-6.75h.007v.008h-.007v-.008zm0 2.25h.007v.008h-.007V13.5zm0 2.25h.007v.008h-.007v-.008zm0 2.25h.007v.008h-.007V18zm2.504-6.75h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V13.5zm0 2.25h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V18zm2.498-6.75h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V13.5zM8.25 6h7.5v2.25h-7.5V6zM12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25z'
		},
		{
			title: 'Договор',
			description:
				'После утверждения финального проекта мы подписываем официальный договор, в котором строго фиксируются стоимость заказа, гарантии и сроки изготовления вашей мебели.',
			icon: 'M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z'
		}
	];
</script>

<svelte:head>
	<title>Как заказать мебель — ЗОВ | Оформление заказа шаг за шагом</title>
	<meta
		name="description"
		content="Пошаговая инструкция по оформлению заказа на фабрике ЗОВ. От бесплатной консультации и дизайн-проекта до заключения договора."
	/>
</svelte:head>

<!-- ==================== HERO SECTION ==================== -->
<section class="relative min-h-[60vh] overflow-hidden bg-surface" id="hero">
	<!-- Background Image -->
	<div class="absolute inset-0">
		<img
			src="/images/hero-kitchen.png"
			alt="Процесс заказа кухни"
			class="h-full w-full object-cover transition-transform duration-[2s]"
			class:scale-105={heroVisible}
		/>
		<div class="absolute inset-0 bg-gradient-to-r from-surface via-surface/90 to-surface/40"></div>
	</div>

	<!-- Content -->
	<div class="relative z-10 flex min-h-[60vh] items-center pt-20 pb-16">
		<div class="mx-auto w-full max-w-7xl px-6">
			<div class="max-w-2xl">
				<!-- Label -->
				<div
					class="mb-6 opacity-0"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.3s"
				>
					<span
						class="inline-flex items-center gap-2 border border-secondary/30 bg-white/60 px-4 py-2 text-[11px] tracking-[0.25em] text-secondary uppercase backdrop-blur-sm"
					>
						Для покупателей
					</span>
				</div>

				<!-- Heading -->
				<h1
					class="text-5xl leading-[1.1] font-light text-primary opacity-0 md:text-6xl lg:text-7xl"
					style="font-family: var(--font-heading); animation-delay: 0.5s"
					class:animate-fade-up={heroVisible}
				>
					Как сделать
					<br />
					<span class="font-normal text-secondary">заказ мебели?</span>
				</h1>

				<!-- Description -->
				<p
					class="mt-8 max-w-lg text-base leading-relaxed text-secondary opacity-0 md:text-lg"
					class:animate-fade-up={heroVisible}
					style="animation-delay: 0.7s"
				>
					Путь к идеальной мебели начинается здесь. Мы продумали каждый шаг, чтобы процесс заказа
					был для вас максимально простым, прозрачным и комфортным.
				</p>
			</div>
		</div>
	</div>

	<!-- Scroll Indicator -->
	<div
		class="absolute bottom-10 left-1/2 -translate-x-1/2 opacity-0"
		class:animate-fade-in={heroVisible}
		style="animation-delay: 1s"
	>
		<div class="flex flex-col items-center gap-2">
			<div class="h-10 w-px bg-gradient-to-b from-primary/30 to-transparent"></div>
		</div>
	</div>
</section>

<!-- ==================== STEPS SECTION ==================== -->
<section
	class="relative overflow-hidden bg-surface-warm py-section lg:py-40"
	id="steps-section"
	data-animate
>
	<!-- Subtle Background Pattern -->
	<div
		class="absolute inset-0 opacity-[0.03]"
		style="background-image: url('data:image/svg+xml,%3Csvg width=\'60\' height=\'60\' viewBox=\'0 0 60 60\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cg fill=\'none\' fill-rule=\'evenodd\'%3E%3Cg fill=\'%232c2c2c\'%3E%3Cpath d=\'M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z\'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E');"
	></div>

	<div class="relative mx-auto max-w-5xl px-6">
		<div
			class="mb-16 text-center opacity-0 transition-all duration-700 md:mb-24"
			class:animate-fade-up={sections['steps-section']}
		>
			<h2
				class="text-3xl font-light text-primary md:text-5xl"
				style="font-family: var(--font-heading);"
			>
				Пошаговый путь к <span class="text-secondary">кухне мечты</span>
			</h2>
		</div>

		<!-- Vertical Timeline -->
		<div class="relative">
			<!-- Timeline Line -->
			<div
				class="absolute top-8 bottom-8 left-6 w-px bg-gradient-to-b from-transparent via-border-medium to-transparent md:left-1/2 md:-translate-x-1/2"
			></div>

			{#each steps as step, i}
				<div
					class="relative mb-16 flex flex-col md:mb-24 md:flex-row md:items-center md:justify-between {i %
						2 ===
					0
						? 'md:flex-row-reverse'
						: ''}"
					class:opacity-0={!sections['steps-section']}
					class:animate-fade-up={sections['steps-section']}
					style="animation-delay: {0.2 + i * 0.15}s"
				>
					<!-- Icon & Mobile Line Anchor -->
					<div
						class="absolute top-0 left-6 flex h-16 w-16 -translate-x-1/2 items-center justify-center rounded-full border-4 border-surface-warm bg-white shadow-card md:left-1/2"
					>
						<span class="text-xs font-semibold tracking-wider text-accent">0{i + 1}</span>
					</div>

					<!-- Content Space (Empty side for alternating layout) -->
					<div class="hidden md:block md:w-1/2"></div>

					<!-- Content Box -->
					<div
						class="ml-16 md:ml-0 md:w-1/2 {i % 2 === 0 ? 'md:pr-16 lg:pr-20' : 'md:pl-16 lg:pl-20'}"
					>
						<div
							class="group relative overflow-hidden bg-white p-8 shadow-card transition-all duration-500 hover:-translate-y-1 hover:shadow-elevated lg:p-10"
						>
							<!-- Decorative Corner Accent -->
							<div
								class="absolute -top-12 -right-12 h-24 w-24 rounded-full bg-surface-warm opacity-50 transition-transform duration-500 group-hover:scale-150"
							></div>

							<svg
								class="relative mb-6 h-8 w-8 text-accent/80 transition-colors duration-500 group-hover:text-secondary"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
								stroke-width="1"
							>
								<path stroke-linecap="round" stroke-linejoin="round" d={step.icon} />
							</svg>

							<h3
								class="relative text-2xl font-medium text-primary transition-colors duration-300 group-hover:text-secondary"
								style="font-family: var(--font-heading);"
							>
								{step.title}
							</h3>

							<div
								class="relative mt-4 h-px w-12 bg-accent/30 transition-all duration-500 group-hover:w-24 group-hover:bg-secondary"
							></div>

							<p class="relative mt-5 text-sm leading-relaxed text-secondary lg:text-base">
								{step.description}
							</p>
						</div>
					</div>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- ==================== CTA SECTION ==================== -->
<section
	class="relative overflow-hidden bg-primary py-section-sm lg:py-section"
	id="cta-section"
	data-animate
>
	<!-- Decorative Elements -->
	<div class="absolute top-0 left-0 h-32 w-32 border border-white/5 lg:h-64 lg:w-64"></div>
	<div class="absolute right-0 bottom-0 h-48 w-48 border border-white/5 lg:h-80 lg:w-80"></div>

	<div class="relative mx-auto max-w-3xl px-6 text-center">
		<div class="opacity-0" class:animate-fade-up={sections['cta-section']}>
			<span class="text-[11px] tracking-[0.3em] text-accent uppercase">Готовы начать?</span>
			<h2
				class="mt-4 text-4xl font-light text-white lg:text-6xl"
				style="font-family: var(--font-heading);"
			>
				Сделайте <span class="text-accent-light">первый шаг</span>
			</h2>
			<p class="mx-auto mt-6 max-w-lg text-base leading-relaxed text-white/60">
				Запишитесь на бесплатную консультацию. Наш дизайнер учтет все нюансы и поможет составить
				идеальный проект мебели.
			</p>
			<div class="mt-10 flex flex-col items-center justify-center gap-4">
				<button
					onclick={() => (isConsultationModalOpen = true)}
					class="inline-flex w-full cursor-pointer items-center justify-center gap-2 border border-white/20 px-8 py-4 text-xs tracking-[0.15em] text-white uppercase transition-all duration-500 hover:border-white/50 sm:w-auto rounded-sm"
				>
					Бесплатная консультация
				</button>
				<div class="flex w-full flex-col items-center justify-center gap-4 sm:w-auto sm:flex-row">
					<a
						href="/showrooms"
						class="inline-flex w-full cursor-pointer items-center justify-center gap-2 border border-white/20 px-8 py-4 text-xs tracking-[0.15em] text-white uppercase transition-all duration-500 hover:border-white/50 sm:w-auto rounded-sm"
					>
						Записаться в салон
					</a>
					<button
						onclick={() => (isDesignerModalOpen = true)}
						class="inline-flex w-full cursor-pointer items-center justify-center gap-2 border border-white/20 px-8 py-4 text-xs tracking-[0.15em] text-white uppercase transition-all duration-500 hover:border-white/50 sm:w-auto rounded-sm"
					>
						Вызвать дизайнера
					</button>
				</div>
			</div>
		</div>
	</div>
</section>

<!-- Modals -->
<Modal bind:showModal={isDesignerModalOpen} title="Вызов дизайнера">
	<DesignerForm onSuccess={() => (isDesignerModalOpen = false)} />
</Modal>

<Modal bind:showModal={isConsultationModalOpen} title="Бесплатная консультация">
	<ConsultationForm onSuccess={() => (isConsultationModalOpen = false)} />
</Modal>
