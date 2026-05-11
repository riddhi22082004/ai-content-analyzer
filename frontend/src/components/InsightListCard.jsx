const InsightListCard = ({
  title,
  items,
  type = "normal"
}) => {

  let styles = `
    bg-slate-900
    border
    border-slate-800
  `;

  if (type === "positive") {

    styles = `
      bg-green-500/10
      border
      border-green-500/20
    `;
  }

  if (type === "negative") {

    styles = `
      bg-red-500/10
      border
      border-red-500/20
    `;
  }

  return (

    <div
      className={`
        ${styles}
        rounded-3xl
        p-6
      `}
    >

      <h2 className="text-2xl font-bold mb-6">
        {title}
      </h2>

      <div className="space-y-4">

        {items?.map((item, index) => (

          <div
            key={index}
            className="
              text-slate-300
              leading-7
            "
          >
            • {item}
          </div>
        ))}

      </div>

    </div>
  );
};

export default InsightListCard;