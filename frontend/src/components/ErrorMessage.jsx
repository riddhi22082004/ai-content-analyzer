const ErrorMessage = ({ message }) => {

  return (

    <div
      className="
        mt-6
        p-4
        rounded-2xl
        bg-red-500/10
        border
        border-red-500/20
        text-red-300
      "
    >

      {message}

    </div>
  );
};

export default ErrorMessage;