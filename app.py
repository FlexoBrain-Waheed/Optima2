function createFlexoPresentation() {
  // إنشاء ملف جديد في جوجل درايف بالاسم الجديد
  var presentation = SlidesApp.create("Strategic Investment Evaluation - Flexo Consultation Services");
  
  // Slide 1: Title Slide (تم تحديث الاسم والشركة هنا)
  var slide1 = presentation.appendSlide(SlidesApp.PredefinedLayout.TITLE);
  slide1.getShapes()[0].getText().setText("Strategic Investment Evaluation");
  slide1.getShapes()[1].getText().setText("SOMA Optima 2 vs. W&H Alphaflex\n\nPresented by Flexo Consultation Services | Waheed Alkarraein");

  // Slide 2: Market Positioning
  var slide2 = presentation.appendSlide(SlidesApp.PredefinedLayout.TITLE_AND_BODY);
  slide2.getShapes()[0].getText().setText("The Paradigm Shift: Flagship vs. Economy");
  slide2.getShapes()[1].getText().setText(
    "• W&H Alphaflex (Economy Class): Positioned as an 'Entry-Level' press. Stripped down to fit lower budgets.\n\n" +
    "• SOMA Optima 2 (Flagship Class): The absolute pinnacle of SOMA’s technology. A fully-equipped, premium machine.\n\n" +
    "• The Strategic Question: Does it make sense to pay over €2 Million for a stripped-down economy model when you can own top-tier technology for the same budget?"
  );

  // Slide 3: Technological Maturity
  var slide3 = presentation.appendSlide(SlidesApp.PredefinedLayout.TITLE_AND_BODY);
  slide3.getShapes()[0].getText().setText("Proven Reliability vs. The Testing Ground");
  slide3.getShapes()[1].getText().setText(
    "• SOMA Optima 2: A mature, 100% reliable platform. Built on deep operational experience with zero structural flaws.\n\n" +
    "• W&H Alphaflex: Newly launched in mid-2024. Its economical structure is largely untested in harsh, long-term operational environments.\n\n" +
    "• Conclusion: Never let your factory be the testing ground for a new economy model."
  );

  // Slide 4: Core Technology & Performance
  var slide4 = presentation.appendSlide(SlidesApp.PredefinedLayout.TITLE_AND_BODY);
  slide4.getShapes()[0].getText().setText("Smart Engineering for Maximum Profit");
  slide4.getShapes()[1].getText().setText(
    "• SOMA Optima 2 (Bounce Killer): Uses aerospace-grade Carbon Composite mandrels and integrated Ink Thermal Stabilization (ITS).\n\n" +
    "• W&H Alphaflex: Relies on heavy steel mandrels and lacks an integrated cooling system, leading to potential bouncing and color instability.\n\n" +
    "• Zero Waste Guarantee: SOMA's IRIS topography-based setup drastically reduces setup time and material waste compared to semi-automatic systems."
  );

  // Slide 5: Operator Ergonomics
  var slide5 = presentation.appendSlide(SlidesApp.PredefinedLayout.TITLE_AND_BODY);
  slide5.getShapes()[0].getText().setText("Empowering Your Workforce");
  slide5.getShapes()[1].getText().setText(
    "• SOMA Optima 2: Features 19 kg Lightweight Air Shafts.\n\n" +
    "• W&H Alphaflex: Uses standard, heavy mechanical shafts.\n\n" +
    "• The Result: SOMA dramatically reduces physical strain on operators, ensuring faster, safer, and much more efficient manual roll changes every single shift."
  );

  // Slide 6: Total Cost of Ownership
  var slide6 = presentation.appendSlide(SlidesApp.PredefinedLayout.TITLE_AND_BODY);
  slide6.getShapes()[0].getText().setText("The Hidden Costs of 'Base' Offers");
  slide6.getShapes()[1].getText().setText(
    "• The SOMA Optima 2 is a complete 'Turn-Key' solution ready for immediate high-quality production.\n\n" +
    "• The competitor's offer requires over €200,000 in hidden additions (Cooling, Cameras, Sleeves, Carbon Shafts) to reach the same operational level.\n\n" +
    "• Financial Flexibility: SOMA offers flexible wire transfers (Net), whereas W&H requires a 75% Letter of Credit (L/C), tying up your cash flow and adding heavy bank fees."
  );

  // Slide 7: Partnership & Challenge
  var slide7 = presentation.appendSlide(SlidesApp.PredefinedLayout.TITLE_AND_BODY);
  slide7.getShapes()[0].getText().setText("A Complete Partnership & The SOMA Challenge");
  slide7.getShapes()[1].getText().setText(
    "• Exclusive Turn-Key Package: Special massive discount if investing in the complete suite (Press, S-Mount, Lamiflex, Pluto).\n\n" +
    "• Unbeatable Training: 10 days on-site + 2 extra weeks later + 1 Full Month in Europe at the SOMA factory for your team.\n\n" +
    "• The SOMA Challenge: We invite you to our factory. Bring your most complex printing designs. Watch us set it up and print HD quality with near-zero waste in minutes. Trust what you see, not just ink on paper."
  );
  
  // مسح الشريحة الأولى الفارغة الافتراضية
  var slides = presentation.getSlides();
  if (slides.length > 7) {
    slides[0].remove();
  }
}
