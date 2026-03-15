<script>
	import { onMount } from 'svelte';

	let visible = $state(false);

	onMount(() => {
		visible = true;
	});
</script>

<svelte:head>
	<title>Спасибо за заявку — ЗОВ | От нашей фабрики для вашей семьи</title>
	<meta name="robots" content="noindex, nofollow" />
</svelte:head>

<section class="relative min-h-[90vh] overflow-hidden bg-surface flex items-center justify-center">
	<!-- Background Image -->
	<div class="absolute inset-0">
		<img
			src="/images/showroom.png"
			alt="ЗОВ"
			class="h-full w-full object-cover transition-transform duration-[2s]"
			class:scale-105={visible}
		/>
		<div class="absolute inset-0 bg-white/50 backdrop-blur-[2px]"></div>
	</div>

	<!-- Content -->
	<div class="relative z-10 w-full max-w-2xl mx-6 px-8 py-12 text-center bg-white/85 backdrop-blur-xl shadow-2xl border border-white/60 rounded-3xl md:px-16 md:py-16">
		<!-- Label -->
		<div
			class="mb-6 opacity-0"
			class:animate-fade-up={visible}
			style="animation-delay: 0.3s"
		>
			<span
				class="inline-flex items-center gap-2 border border-secondary/30 px-4 py-2 text-[11px] tracking-[0.25em] text-secondary uppercase"
			>
				Успешно
			</span>
		</div>

		<!-- Heading -->
		<h1
			class="text-4xl leading-[1.1] font-light text-primary opacity-0 md:text-5xl lg:text-6xl"
			style="font-family: var(--font-heading); animation-delay: 0.5s"
			class:animate-fade-up={visible}
		>
			Спасибо за <span class="font-normal text-secondary">доверие</span>
		</h1>

		<!-- Description -->
		<p
			class="mx-auto mt-8 max-w-lg text-base leading-relaxed text-text-secondary opacity-0 md:text-lg"
			class:animate-fade-up={visible}
			style="animation-delay: 0.7s"
		>
			Ваша заявка успешно отправлена. Наши менеджеры свяжутся с вами в ближайшее время для уточнения всех деталей и ответа на ваши вопросы.
		</p>

		<!-- CTA Buttons -->
		<div
			class="mt-10 flex flex-wrap items-center justify-center gap-4 opacity-0"
			class:animate-fade-up={visible}
			style="animation-delay: 0.9s"
		>
			<a
				href="/"
				class="group inline-flex items-center gap-3 border border-primary bg-primary px-8 py-4 text-xs tracking-[0.15em] text-text-inverse uppercase transition-all duration-500 hover:border-secondary hover:bg-secondary"
			>
				<svg class="h-4 w-4 transition-transform duration-300 group-hover:-translate-x-1" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
					<path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18" />
				</svg>
				На главную
			</a>
		</div>
	</div>
</section>
